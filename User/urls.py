from django.urls import path
from .views import favorite, BookmarkedPostsView

urlpatterns = [
    path('liked/post/', favorite.as_view(), name='liked-posts'),
    #     path('api/user/liked/comment/',
    #          LikedCommentsView.as_view(), name='liked-comments'),
    path('bookmark/news/',
         BookmarkedPostsView.as_view(), name='bookmarked-posts'),
    #     path('api/user/bookmark/comment/',
    #          BookmarkedCommentsView.as_view(), name='bookmarked-comments'),
]
