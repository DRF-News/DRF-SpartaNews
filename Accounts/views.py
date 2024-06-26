from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegisterSerializer, UserUpdateSerialzer, ChangePasswordSerializer
from .models import User


@api_view(["POST"])
def register(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountMangement(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        serializer = UserUpdateSerialzer(instance=user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(data=serializer.data)


    def delete(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        if check_password(request.data["password"], user.password):
            user.delete()
            return Response(data={"message":"회원탈퇴 성공"})
        else:
            return Response(data={"message":"비밀번호 불일치"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def change_password(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = ChangePasswordSerializer(data=request.data, context={'request':request})
    if serializer.is_valid(raise_exception=True):
        user.set_password(request.data['new_password'])
        user.save()
    return Response(data={"message":"비밀번호 변경 성공"}, status=status.HTTP_200_OK)