from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts')
    bookmarked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmarked_posts')
    class Meta:
        app_label = 'User'

class Comment(models.Model):
    post = models.ForeignKey('User.Post', related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_comments')
    bookmarked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmarked_comments')
    class Meta:
        app_label = 'User'
