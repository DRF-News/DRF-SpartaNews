from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from Post.serializers import PostSerializer
from Post.models import Post
import trafilatura
from .functions import sn_plus


# @api_view(["POST"])
# # @permission_classes(IsAuthenticated)
# def create_sn_puls(request, ):
#     serializer = PostSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         # url = request.data['url']
#         # html = trafilatura.fetch_url(url)
#         # text = trafilatura.extract(html)
#         # serializer.data['content'] = sn_plus(text)
#         print(serializer.data)
#         serializer.save()
#     return Response(serializer.data)


class SNPlusCreateAPIView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # url = request.data['url']
            # html = trafilatura.fetch_url(url)
            # text = trafilatura.extract(html)
            # serializer.data['content'] = sn_plus(text)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            print(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
