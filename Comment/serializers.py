from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    parent_comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'created_at', 'parent_comment']

    def create(self, validated_data):
        parent_comment = validated_data.pop('parent_comment', None)
        return Comment.objects.create(parent_comment=parent_comment, **validated_data)
