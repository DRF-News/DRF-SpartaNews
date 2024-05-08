from django.urls import path

from . import views

urlpatterns = [
    path("<str:username>/", views.UserDetailAPIView.as_view(), name="user_detail"),
    path("liked/post/", views.Favorite.as_view(), name="liked-posts"),
    path(
        "bookmark/news/", views.BookmarkedPostsView.as_view(), name="bookmarked-posts"
    ),
]
