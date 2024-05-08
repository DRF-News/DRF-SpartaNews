from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Post.serializers import PostSerializer
class Favorite(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # 현재 사용자가 좋아하는 게시물들을 가져옴
        liked_posts = request.user.favorite.all()
        # 게시물 시리얼라이즈
        serializer = PostSerializer(liked_posts, many=True)
        return Response(data=serializer.data)
class BookmarkedPostsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # 현재 사용자가 즐겨찾기한 게시물들을 가져옴
        bookmarked_posts = request.user.bookmarked_posts.all()
        # 게시물 시리얼라이즈
        serializer = PostSerializer(bookmarked_posts, many=True)
        return Response(serializer.data)