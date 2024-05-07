from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from Post.models import Post
from .models import Comment
from .serializers import CommentSerializer


# Comment 작성하기 / 작성 후 해당 게시글에 달린 댓글들 전부 조회회
class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return post.comments.all()

    def create(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            queryset = self.get_queryset()
            return Response(self.serializer_class(queryset, many=True).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Comment 수정하기
class CommentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CommentSerializer

    # Comment 찾기
    def get_object(self):
        post_id = self.kwargs['post_id']
        return get_object_or_404(Comment, post_id=post_id)

    # PUT 요청 처리
    def put(self, request, *args, **kwargs):
        post_id = self.kwargs['post_id']  # post_id 가져오기
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Comment 삭제하기
class CommentDeleteAPIView(generics.DestroyAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return post.comments.all()

    def destroy(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Comment 보여주기 / 해당 게시물에 대한 모든 Comment 조회 가능
class CommentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return post.comments.all()


# reply 달기
class ReplyCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def create(self, request, post_id, comment_id):
        # 부모 댓글을 가져오기
        parent_comment = get_object_or_404(Comment, pk=comment_id)

        # 해당하는 post를 가져옴. 없을 경우 404 에러를 반환
        post = get_object_or_404(Post, pk=post_id)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post, parent_comment=parent_comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Reply 목록 보여주기
class ReplyListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        comment_id = self.kwargs['comment_id']
        parent_comment = get_object_or_404(Comment, pk=comment_id)
        return parent_comment.replies.all()


# Reply 수정하기
class ReplyUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CommentSerializer

    # Comment 찾기
    def get_object(self):
        post_id = self.kwargs['post_id']
        comment_id = self.kwargs['comment_id']
        reply_id = self.kwargs['reply_id']
        return get_object_or_404(Comment, post_id=post_id, parent_comment_id=comment_id, id=reply_id)

    # PUT 요청 처리
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Reply 삭제하기
class ReplyDeleteAPIView(generics.DestroyAPIView):
    serializer_class = CommentSerializer

    # Comment 찾기
    def get_object(self):
        post_id = self.kwargs['post_id']
        comment_id = self.kwargs['comment_id']
        reply_id = self.kwargs['reply_id']
        return get_object_or_404(Comment, post_id=post_id, parent_comment_id=comment_id, id=reply_id)

    # DELETE 요청 처리
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)