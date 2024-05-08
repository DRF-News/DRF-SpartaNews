from rest_framework import generics
from django.db.models import Q
from Post.models import Post
from .serializers import PostSerializer


# class PostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        title = query_params.get("title")
        content = query_params.get("content")
        username = query_params.get("username")

        q = Q()
        if title:
            q &= Q(title__icontains=title)
        if content:
            q &= Q(content__icontains=content)
        if username:
            q &= Q(user__username__icontains=username)

        return Post.objects.filter(q)
