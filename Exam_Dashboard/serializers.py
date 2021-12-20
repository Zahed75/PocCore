from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from django.contrib.auth.hashers import make_password
from .models import *


class ExamPackSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = ExamPack
        fields = '__all__'


class CreatExamSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = CreateExam
        fields = '__all__'


class Question_OneSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = QuestionModel_One
        fields = '__all__'


class Anstype_oneSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = AnswerMode_One

        fields = '__all__'


class CreateQuestionSerializerTwo(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = QuestionModel_Two
        fields = '__all__'


class CreateAnsTypeTwoSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = AnsModel_Two

        fields = '__all__'


class CreateQuestionThreSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = QuesionModel_Three
        fields = '__all__'


class CreateAnsThreeSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = AnsModel_Three
        fields = '__all__'
