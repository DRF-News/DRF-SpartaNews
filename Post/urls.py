from django.urls import path
from .views import (
    PostListAPIView,
    # PostDetailAPIView,
    # PostCreateAPIView,
    # PostFavoriteAPIView,
    # PostBookmarkAPIView,
)

urlpatterns = [
    path('', PostListAPIView.as_view(), name='post-list'),
    # path('create/', PostCreateAPIView.as_view(), name='post-create'),
    # path('<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    # path('<int:pk>/favorite/', PostFavoriteAPIView.as_view(), name='post-favorite'),
    # path('<int:pk>/bookmark/', PostBookmarkAPIView.as_view(), name='post-bookmark'),
]