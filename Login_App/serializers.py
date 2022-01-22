from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from django.contrib.auth.hashers import make_password
from .models import *


class LoginSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=14)
    password = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = [
            'phone_number',
            'password'
        ]


class RegistrationDataSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    password = serializers.CharField(max_length=256)

    class Meta:
        model = UserInfo
        fields = ['phone_number', 'password']


# payload = request.data
#         payload['user'] = request.user.id


class StudentProfileSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'


# class ChangePasswordSerializer(serializers.Serializer):
#     model = UserInfo
#
#     """
#     Serializer for password change endpoint.
#     """
#     phone_number = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)





class PasswordChangeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(style={"input_type": "Phone"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        return value