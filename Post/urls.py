from django.urls import path
from .views import (
    PostListAPIView,
    PostCreateAPIView,
    PostDetailAPIView,
    PostFavoriteAPIView,
    PostBookmarkAPIView,
)

urlpatterns = [
    path('', PostListAPIView.as_view(), name='post-list'),
    path('create/', PostCreateAPIView.as_view(), name='post-create'),
    path('<int:id>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('<int:id>/favorite/', PostFavoriteAPIView.as_view(), name='post-favorite'),
    path('<int:id>/bookmark/', PostBookmarkAPIView.as_view(), name='post-bookmark'),
]