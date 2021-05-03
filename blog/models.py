
from django.db import models
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    # def get_absolute_url(self):
    #     return reverse('blog:detail', args=(self.id, ))

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField('date published', auto_now_add=True)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

