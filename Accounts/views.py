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
    if serializer.is_valid() and request.data["password"] == request.data["confirm_password"]:
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
    serializer = ChangePasswordSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        old_password = request.data['old_password']
        new_password = request.data['new_password']
        confirm_password = request.data['confirm_password']

        if not check_password(old_password, user.password):
            return Response(data={"message":"현재 비밀번호 불일치"}, status=status.HTTP_400_BAD_REQUEST)
        elif new_password != confirm_password:
            return Response(data={"message":"새 비밀번호와 비밀번호 확인 불일치"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user.set_password(new_password)
            user.save()
    return Response(data={"message":"비밀번호 변경 성공"}, status=status.HTTP_200_OK)