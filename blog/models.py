from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
