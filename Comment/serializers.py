from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    # 작성자의 username을 포함하기 위한 추가 필드
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content','author_username', 'created_at', 'parent_comment']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return Comment.objects.create(**validated_data)

