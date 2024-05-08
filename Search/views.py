from rest_framework import generics
from django.db.models import Q
from Post.models import Post
from Accounts.models import User
from Post.serializers import PostSerializer
from User.serializers import UserDetailSerializer


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


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        username = query_params.get("username")
        email = query_params.get("email")
        intro = query_params.get("intro")

        q = Q()
        if username:
            q &= Q(username__icontains=username)
        if email:
            q &= Q(email__icontains=email)
        if intro:
            q &= Q(intro__icontains=intro)

        return User.objects.filter(q)
