from django.shortcuts import render

from rest_framework import generics, status
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response



class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

class PostFavoriteAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.points += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class PostBookmarkAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        instance.bookmarked_by.add(user)
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)