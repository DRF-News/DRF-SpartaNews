from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    favorite_count = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'username', 'url', 'created_at', 'points', 'updated_at', 'content', 'favorite_count']

    def get_username(self, obj):
        return obj.user.username

    def get_favorite_count(self, obj):
        return obj.favorite.count()