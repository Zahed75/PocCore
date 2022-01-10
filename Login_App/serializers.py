from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from django.contrib.auth.hashers import make_password
from .models import *
import base64


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
    class Meta:
        model = StudentProfile
        fields = '__all__'


#
class ChangePasswordSerializer(serializers.Serializer):
    model = UserInfo

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

#
# class Base64ImageField(serializers.ImageField):
#
#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64
#         import six
#         import uuid
#
#         if isinstance(data, six.string_types):
#             if 'data:' in data and ';base64,' in data:
#                 header, data = data.split(';base64,')
#
#             try:
#                 decoded_file = base64.b64decode(data)
#             except TypeError:
#                 self.fail('invalid_image')
#
#             file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
#             file_extension = self.get_file_extension(file_name, decoded_file)
#             complete_file_name = "%s.%s" % (file_name, file_extension,)
#             data = ContentFile(decoded_file, name=complete_file_name)
#
#         return super(Base64ImageField, self).to_internal_value(data)
#
#     def get_file_extension(self, file_name, decoded_file):
#         import imghdr
#
#         extension = imghdr.what(file_name, decoded_file)
#         extension = "jpg" if extension == "jpeg" else extension
#
#         return extension


# class StudentProfileSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
#     # Profile_image = Base64ImageField()
#
#     class Meta:
#         model = StudentProfile
#         fields = '__all__'
#
