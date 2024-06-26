from django.urls import path
from .views import CommentListCreateAPIView, CommentRetrieveAPIView, ReplyCreateAPIView, CommentUpdateAPIView, CommentDeleteAPIView, ReplyListAPIView, ReplyUpdateAPIView, ReplyDeleteAPIView

urlpatterns = [
    path('<int:post_id>/', CommentListCreateAPIView.as_view(), name='comment_list_create'),
    path('<int:post_id>/', CommentRetrieveAPIView.as_view(), name='comment_retrieve'),
    path('<int:post_id>/update/<int:comment_id>/', CommentUpdateAPIView.as_view(), name='comment_update'),
    path('<int:post_id>/delete/<int:comment_id>/', CommentDeleteAPIView.as_view(), name='comment_delete'),
    path('<int:post_id>/<int:comment_id>/reply/', ReplyCreateAPIView.as_view(), name='reply_create'),
    path('<int:post_id>/<int:comment_id>/replylist/', ReplyListAPIView.as_view(), name='reply_retrieve'),
    path('<int:post_id>/<int:comment_id>/reply/<int:reply_id>/', ReplyUpdateAPIView.as_view(), name='reply_update'),
    path('<int:post_id>/<int:comment_id>/reply/<int:reply_id>/delete/', ReplyDeleteAPIView.as_view(), name='reply_delete'),
]