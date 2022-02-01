import random
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from django.contrib.auth.hashers import make_password
from .models import *
from Login_App.models import *
from Student_ExamDashboard.models import *
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
        model = QuestionModel_One
        fields = '__all__'


class CreateQuestionModelTwoSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = QuestionModel_Two
        fields = '__all__'


class CreateQuestionModelThreeSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = QuestionModel_Three
        fields = '__all__'


class CreateQuestionModelThreeSerializer_Sub(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    question_one = CreateQuestionModelThreeSerializer(read_only=True, many=True)

    class Meta:
        model = QuestionModel_Three_Sub
        fields = '__all__'


class Anstype_oneSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = AnswerModel_One

        fields = '__all__'


class CreateAnsTypeTwoSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = AnsModel_Two

        fields = '__all__'


class CreateAnsThreeSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = AnsModel_Three
        fields = '__all__'


class CreateAnsThreeSerializer_Sub(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = AnsModel_Three
        fields = '__all__'


class ExamResultSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = '__all__'


class AllStudentResultSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = AllStudentResult
        fields = '__all__'


class CreateBatchSettings(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = BatchSettings
        fields = '__all__'


class StudentProfileSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'
        # depth = 1


class UserInfoSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
        # depth = 1
    def get_serializer_context(self):
        context = super().get_serializer_context()
        depth = 0
        try:
            depth = int(self.request.query_params.get('depth', 0))
        except ValueError:
            pass # Ignore non-numeric parameters and keep default 0 depth
        
        context['depth'] = depth
