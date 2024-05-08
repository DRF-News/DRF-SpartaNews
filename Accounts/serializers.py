from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    intro = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'email', 'intro']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password', None)
        
        if not password:
            raise serializers.ValidationError("비밀번호를 입력해주세요.")
        if password != confirm_password:
            raise serializers.ValidationError("비밀번호가 서로 일치하지 않습니다.")
        validate_password(password)
        return data


class UserUpdateSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['username', 'password']


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        user = self.context['request'].user
        password = data.get('new_password')
        
        if not password:
            raise serializers.ValidationError("비밀번호를 입력해주세요.")
        
        validate_password(password, user)
        return data