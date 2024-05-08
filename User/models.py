from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    liked_by = models.ManyToManyField(User, related_name='liked_posts')
    bookmarked_by = models.ManyToManyField(User, related_name='bookmarked_posts')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    liked_by = models.ManyToManyField(User, related_name='liked_comments')
    bookmarked_by = models.ManyToManyField(User, related_name='bookmarked_comments')
