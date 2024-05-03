from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    points = models.IntegerField(default=0)
    favorite = models.BooleanField(default=False)
    bookmark = models.BooleanField(default=False)

    def __str__(self):
        return self.title