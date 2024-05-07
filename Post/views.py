from django.shortcuts import render

from rest_framework import generics, status
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView



class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostFavoriteAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    
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
    permission_classes = [IsAuthenticated]
    
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