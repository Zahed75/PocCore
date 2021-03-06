import random
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from django.contrib.auth.hashers import make_password
from .models import *
from Login_App.models import *
from Exam_Dashboard.models import *


# from Exam_Dashboard.serializers import *

class ExamPackSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = ExamPack
        fields = '__all__'


class CreatExamSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    # exam_id = serializers.CharField(max_length=40)

    class Meta:
        model = CreateExam
        fields = '__all__'


class CreateQuestionModelOneSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = QuestionModel_One
        fields = '__all__'


class CreateQuestionModelTwoSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = QuestionModel_Two
        fields = '__all__'


# class CreateQuestionModelThreeSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
#     class Meta:
#         model = QuestionModel_Three
#         fields = '__all__'


# class CreateQuestionModelOneSerializer(serializers.Serializer):
#     question_name = serializers.CharField(max_length=4000)
#     q_image = serializers.ImageField()
#     marks = serializers.IntegerField(default=5)


class ExamResultSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = '__all__'


class AllStudentResultSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = AllStudentResult
        fields = '__all__'
