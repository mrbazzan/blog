
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Post
# Create your views here.


class BlogListView(generic.ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'


class BlogPostView(generic.CreateView):
    model = Post
    template_name = 'blog/new.html'
    success_url = reverse_lazy('blog:home')
    fields = ['title', 'author', 'body']


class BlogUpdateView(generic.UpdateView):
    model = Post
    template_name = 'blog/edit.html'
    success_url = reverse_lazy('blog:home')
    fields = ['title', 'body']


class BlogDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:home')
    fields = ['title', 'author', 'body']
