from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from django.contrib.auth.hashers import make_password
from .models import *


class ExamPackSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    cover_photo=serializers.ImageField()
    class Meta:
        model = ExamPack
        fields = '__all__'
