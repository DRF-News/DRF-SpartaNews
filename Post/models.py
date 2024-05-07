from django.db import models
from Accounts.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    points = models.IntegerField(default=0, null=True)
    favorite = models.ManyToManyField(User, related_name='favorite')
    bookmark = models.ManyToManyField(User, related_name='bookmark')

    def __str__(self):
        return self.title