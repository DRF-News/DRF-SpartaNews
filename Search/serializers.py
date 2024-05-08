from rest_framework import serializers
from Post.models import Post


class PostSerializer(serializers.ModelSerializer):
    favorite_count = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_username(self, obj):
        return obj.user.username

    def get_favorite_count(self, obj):
        return obj.favorite.count()
