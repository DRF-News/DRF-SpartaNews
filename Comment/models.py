from django.conf import settings
from django.db import models
from Post.models import Post


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey(
        'self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post}"