from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from .models import User

@api_view(["POST"])
def register(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid() and request.data["password"] == request.data["confirm_password"]:
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountMangement(APIView):
    def post(self, request, user_id):
        pass

    def delete(self, request, user_id):
        user = get_object_or_404(pk=user_id)
        if check_password(request.data["password"], user.password):
            user.delete()
            return Response(data={"message":"회원탈퇴 성공"}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(data={"message":"비밀번호 불일치"}, status=status.HTTP_400_BAD_REQUEST)
