
from django.shortcuts import render
from django.db.utils import IntegrityError

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.views import generic
from config.settings import EMAIL_HOST_USER
from django.urls import reverse, reverse_lazy

from .models import Post, Comment
from . import forms


# Create your views here.


class BlogListView(generic.ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(generic.DetailView):
    context_object_name = 'detail'
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        try:
            context['comment_list'] = Comment.objects.filter(post_id=self.kwargs['pk'])
        except Comment.DoesNotExist:
            context['comment_list'] = None
        return context


class BlogPostView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'blog/new.html'
    success_url = reverse_lazy('blog:home')
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author_id = self.request.POST.get('author')
        return super(BlogPostView, self).form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    template_name = 'blog/edit.html'
    success_url = reverse_lazy('blog:home')
    fields = ['title', 'body']
    permission_denied_message = 'You do not have permission to edit this page.'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(UserPassesTestMixin, LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:home')
    fields = ['title', 'author', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogCommentView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    template_name = 'blog/comment.html'
    fields = ['comment']

    def get_success_url(self):
        success_url = reverse_lazy('blog:detail', args=(self.kwargs['pk'],))
        return success_url

    def form_valid(self, form):
        form.instance.name_id = self.request.POST.get('name')
        form.instance.post_id = self.kwargs['pk']
        return super(BlogCommentView, self).form_valid(form)


def register(request):
    error_message = None
    sub = forms.EmailForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('Email')

        if not username:
            error_message = 'Username cannot be blank'
        elif not password:
            error_message = 'Password cannot be blank'
        elif not email:
            error_message = 'Email cannot be blank'

        if error_message is None:
            try:
                User.objects.create_user(
                    username=username,
                    password=password,
                    email=email
                )
            except IntegrityError:
                error_message = 'User {} is already registered'.format(username)
            else:
                return HttpResponseRedirect(reverse('login'))

    return render(request, 'registration/register.html', {
        'error_message': error_message,
        'form': sub,
    })
