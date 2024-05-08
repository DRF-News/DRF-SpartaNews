from django.urls import path
from .views import PostListAPIView, UserListAPIView


urlpatterns = [
    path("", PostListAPIView.as_view(), name="post-list"),
    path("user/", UserListAPIView.as_view(), name="user-list"),
]
