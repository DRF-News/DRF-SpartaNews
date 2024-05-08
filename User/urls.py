from django.urls import path
from .views import LikedPostsView, LikedCommentsView, BookmarkedPostsView, BookmarkedCommentsView

urlpatterns = [
    path('api/user/liked/post/', LikedPostsView.as_view(), name='liked-posts'),
    path('api/user/liked/comment/',
         LikedCommentsView.as_view(), name='liked-comments'),
    path('api/user/bookmark/news/',
         BookmarkedPostsView.as_view(), name='bookmarked-posts'),
    path('api/user/bookmark/comment/',
         BookmarkedCommentsView.as_view(), name='bookmarked-comments'),
]
