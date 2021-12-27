import random
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from django.contrib.auth.hashers import make_password
from .models import *
from Login_App.models import *
from Exam_Dashboard.models import *


class ExamPackSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = ExamPack
        fields = '__all__'