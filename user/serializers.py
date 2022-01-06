from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from django.contrib.auth.hashers import make_password
from .models import *


class CreateCustomSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
