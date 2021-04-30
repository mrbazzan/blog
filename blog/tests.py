from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


# Create your tests here.
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

    @staticmethod
    def text_string_representation(self):
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(self.post.title, 'Test Title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(self.post.body, 'Body of the Test')

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'of the Test')
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('blog:detail', args=(1, )))
        no_response = self.client.get(reverse('blog:detail', args=(2, )))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test Title')
        self.assertTemplateUsed(response, 'blog/detail.html')
