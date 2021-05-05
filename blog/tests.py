from django.test import TestCase, Client
from django.test.utils import ignore_warnings
from django.contrib.auth import get_user_model
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Post

ignore_warnings(message="No directory at", module="whitenoise.base").enable()


class BlogTest(TestCase):
    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='password'
        )
        self.post = Post.objects.create(
            title='Test Title',
            body='Body of the Test',
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)

    def test_blog_content(self):
        print(self)
        self.assertEqual(self.post.title, 'Test Title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(self.post.body, 'Body of the Test')

    def test_blog_list_view(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'of the Test')
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_blog_detail_view(self):
        response = self.client.get(reverse('blog:detail', args=(1, )))
        no_response = self.client.get(reverse('blog:detail', args=(2, )))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test Title')
        self.assertTemplateUsed(response, 'blog/detail.html')


class BlogAuthentication(TestCase):

    def setUp(self):
        self.user = get_user_model()
        self.test_user = self.user.objects.create_user(username='test', password='test')

    def test_register(self):
        self.assertEqual(self.client.get(reverse('blog:register')).status_code, 200)
        response = self.client.post(
            reverse('blog:register'),
            data={'username': 'p', 'password': 'p'}
        )
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.wsgi_request.POST['username'], 'p')
        assert get_user_model().objects.get(username='p') is not None

    def test_validate_input_username(self):
        response = self.client.post(
            reverse('blog:register'),
            data={'username': '', 'password': ''})
        self.assertContains(response, "Username cannot be blank")

    def test_validate_input_password(self):
        response = self.client.post(
            reverse('blog:register'),
            data={'username': 'p', 'password': ''})
        self.assertContains(response, "Password cannot be blank")

    def test_validate_input_already_registered(self):
        response = self.client.post(
            reverse('blog:register'),
            data={'username': 'test', 'password': 'test'}
        )
        self.assertContains(response, "is already registered")

    def test_login(self):
        self.assertEqual(self.client.get(reverse('login')).status_code, 200)
        _ = self.client.login(username='test', password='test')
        self.assertEqual(_, True)

        response = self.client.get('/')
        self.assertContains(response, 'test')
        self.assertContains(response, 'Logout')

        request = response.wsgi_request
        self.assertEqual(request.session.get('_auth_user_id'), str(self.test_user.id))

    def test_login_validate_username(self):
        response = self.client.post(
            reverse('login'),
            data={'username': '', 'password': ''})
        self.assertContains(response, "Your username and password did not match.")

    def test_login_validate_password(self):
        response = self.client.post(
            reverse('login'),
            data={'username': 'p', 'password': ''})
        self.assertContains(response, "Your username and password did not match.")

    def logout(self):
        _ = self.client.logout()
        self.assertEqual(type(_), type(None))

        response = self.client('/')
        request = response.wsgi_request
        self.assertEqual(dict(request.session), {})
        assert self.test_user.id not in request.session


class BlogHomePage(TestCase):
    def __init__(self, response):
        super(BlogHomePage, self).__init__(response)
        self.response = None

    def setUp(self):
        self.response = self.client.get(reverse('blog:home'))

    def test_index(self):
        self.assertContains(self.response, 'Login')
        self.assertContains(self.response, 'Register')
        self.assertEqual(self.response.status_code, 200)

# TODO: I need to write more tests
