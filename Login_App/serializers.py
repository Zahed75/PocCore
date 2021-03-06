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
            'password',

        ]
        depth = 1


class RegistrationDataSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    password = serializers.CharField(max_length=256)

    class Meta:
        model = UserInfo
        fields = ['phone_number', 'password', 'is_block']
        depth = 1


# payload = request.data
#         payload['user'] = request.user.id


class StudentProfileSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'

        # depth=1
