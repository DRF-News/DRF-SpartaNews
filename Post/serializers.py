from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    favorite_count = serializers.SerializerMethodField()
        
    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'created_at', 'points', 'updated_at', 'content', 'favorite_count', 'bookmark']
        
    def get_favorite_count(self, obj):
        return obj.favorite.count()