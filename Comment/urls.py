from django.urls import path
from .views import CommentListCreateAPIView

urlpatterns = [
    path('<int:post_id>/', CommentListCreateAPIView.as_view(), name='comment_list_create'),
]
