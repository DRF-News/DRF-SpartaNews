from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserDetailSerializer


class UserDetailAPIView(APIView):
    def get(self, request, username):
        user = get_object_or_404(get_user_model(), username=username)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
