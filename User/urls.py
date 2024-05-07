from django.urls import path

from . import views

urlpatterns = [
    path("<str:username>/", views.UserDetailAPIView.as_view(), name="user_detail"),
]
