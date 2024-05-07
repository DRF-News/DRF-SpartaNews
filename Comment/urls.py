from django.urls import path
from .views import CommentListCreateAPIView, CommentRetrieveAPIView, ReplyCreateAPIView, CommentUpdateAPIView, CommentDeleteAPIView

urlpatterns = [
    path('<int:post_id>/', CommentListCreateAPIView.as_view(), name='comment_list_create'),
    path('<int:post_id>/', CommentRetrieveAPIView.as_view(), name='comment_retrieve'),
    path('<int:post_id>/update', CommentUpdateAPIView.as_view(), name='comment_update'),
    path('<int:post_id>/delete', CommentDeleteAPIView.as_view(), name='comment_delete'),
    path('<int:post_id>/<int:comment_id>/reply/', ReplyCreateAPIView.as_view(), name='reply_create'),
]