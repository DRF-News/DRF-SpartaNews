from django.urls import path
from .views import Favorite, BookmarkedPostsView
urlpatterns = [
    path('liked/post/', Favorite.as_view(), name='liked-posts'),
    path('bookmark/news/', BookmarkedPostsView.as_view(), name='bookmarked-posts'),
]