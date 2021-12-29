import random
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from django.contrib.auth.hashers import make_password
from .models import *
from Login_App.models import *


class ExamPackSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = ExamPack
        fields = '__all__'


class CreatExamSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    # exam_id = serializers.CharField(max_length=40)

    class Meta:
        model = CreateExam
        fields = '__all__'


class StudentProfileSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'


class CreateQuestionModelOneSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = Question_model_one
        fields = '__all__'


class CreateQuestionModelTwoSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = Question_model_two
        fields = '__all__'


class CreateQuestionModelThreeSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = Question_model_three
        fields = '__all__'
