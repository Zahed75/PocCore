from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from django.contrib.auth.hashers import make_password
from .models import *
# from drf_extra_fields.fields import Base64ImageField


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
    # image=Base64ImageField(max_length=None, use_url=True, )
    class Meta:
        model = StudentProfile
        fields = '__all__'
        # image = Base64ImageField(required=False)


#
class ChangePasswordSerializer(serializers.Serializer):
    model = UserInfo

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
