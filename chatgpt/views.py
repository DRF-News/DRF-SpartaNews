from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import trafilatura
from Post.serializers import PostSerializer
from .functions import sn_plus

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_snplus(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.validated_data['user'] = request.user
        url = request.data.get('url')

        if not url:
            return Response({"error": "요약할 url이 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        html = trafilatura.fetch_url(url)
        text = trafilatura.extract(html)

        if not text:
            return Response({"error": "해당 url은 요약할 수 없습니다."}, status=status.HTTP_400_BAD_REQUEST)

        summary = sn_plus(text)
        serializer.validated_data["content"] += ('\n SN+의 요약 : ' + summary)
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
