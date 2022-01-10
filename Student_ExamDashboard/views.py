from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import login
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework import status
from rest_framework.serializers import Serializer
from .models import *
from Login_App.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.utils import json
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken, UntypedToken, Token
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from json import dumps, loads, JSONEncoder, JSONDecoder
from Exam_Dashboard.models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser
from django.views.decorators.csrf import csrf_exempt
import random
import string
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, \
    IsAdminUser, DjangoModelPermissions


# Create your views here.


@api_view(['GET'])
@parser_classes([MultiPartParser])
@permission_classes([IsAuthenticated])
def get_exam_pack(request):
    user = request.user
    print(user)
    student = StudentProfile.objects.get(user=user)
    print(student.level)
    try:
        exam_pack = ExamPack.objects.filter(level=student.level)
        print(exam_pack)
        data_serializer = ExamPackSerializer(exam_pack, many=True)

        return Response({
            'code': status.HTTP_200_OK,
            'message': 'List of all ExamPack of level Wise',
            'data': data_serializer.data

        })



    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
@parser_classes([MultiPartParser])
@permission_classes([IsAuthenticated])
def ExamList(request):
    user = request.user
    student = StudentProfile.objects.get(user=user)

    try:
        exam_list = ExamPack.objects.filter(level=student.level)
        queryset = CreateExam.objects.filter(exam_pack__in=exam_list)
        data_serializer = CreatExamSerializer(queryset, many=True)

        return Response({
            'code': status.HTTP_200_OK,
            'message': 'List of all ExamPack of level Wise',
            'data': data_serializer.data

        })



    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
@parser_classes([MultiPartParser])
@permission_classes([IsAuthenticated])
def get_question(request, exam_id):
    try:
        from django.core import serializers

        question_type_one = CreateQuestionModelOneSerializer(QuestionModel_One.objects.filter(exam_name=exam_id),
                                                             many=True)
        print(question_type_one)
        question_type_two = CreateQuestionModelTwoSerializer(QuestionModel_Two.objects.filter(exam_name=exam_id),
                                                             many=True)
        question_type_three = CreateQuestionModelThreeSerializer(QuestionModel_Three.objects.filter(exam_name=exam_id),
                                                                 many=True)

        data_dict = {
            "data_one": question_type_one.data,
            "data_two": question_type_two.data,
            "data_three": question_type_three.data
        }

        return Response({
            'code': status.HTTP_200_OK,
            'message': 'List of all ExamPack of level Wise',
            'question_data': data_dict,

        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['POST', 'GET'])
@parser_classes([MultiPartParser])
def ans_validation(request):
    question_name = request.data['question']
    answer_by_user = request.data['ans']
    # print(answer_by_user)

    try:

        question_one = QuestionModel_One.objects.filter(question_name=question_name)
        question_two = QuestionModel_Two.objects.filter(question_name=question_name)
        question_three = QuestionModel_Three.objects.filter(question_name=question_name)

        # print(question_one)
        # print(question_two)
        # print(question_three)

        question = None
        question_id = None

        question_model_array = [question_one, question_two, question_three]

        for questions in question_model_array:
            if len(questions) == 1:
                question = questions
            else:
                pass

        # for item in question:
        #     question_id = item.id

        # print(question)
        # print(question_id)

        ans_one = AnswerModel_One.objects.filter(Question__question_name=question_name)
        print(ans_one)
        ans_two = AnsModel_Two.objects.filter(Question__question_name=question_name)
        print(ans_two)
        ans_three = AnsModel_Three.objects.filter(Question__question_name=question_name)
        print(ans_three)

        # print(ans_one)
        # print(ans_two)
        # print(ans_three)

        ans_model_array = [ans_one, ans_two, ans_three]

        answer = None

        for item in ans_model_array:
            if len(item) > 0:
                answer = item
            else:
                pass

        ans_is_right = False

        for item in answer:
            if answer_by_user == item.ans and item.is_correct:
                ans_is_right = True
                print("Right")
                break
            else:
                print("Wrong")
                ans_is_right = False

        if ans_is_right == True:
            print("Right ans")
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'Answer is right'
            })

        else:
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'Answer is wrong'
            })

        # return Response({
        #     'code': status.HTTP_200_OK,
        #     'message': 'Ans Validate!',
        #     # 'data': data_serializer.data
        # })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
@parser_classes([MultiPartParser])
def get_report(request):
    permission_classes([IsAdminUser])
    # user = request.user
    # student = CreateExam.objects.filter()
    # print(student)
    try:
        report_info = ExamResult.objects.filter(student=request.user)
        data_serializer = ExamResultSerializer(report_info, many=True)
        print(data_serializer)
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'All Student Report!',
            'data': data_serializer.data
        })


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser])
def all_student_result(request, exam_name):
    if request.method == 'GET':
        try:
            report = AllStudentResult.objects.filter(exam_name__Exam_name=exam_name)
            data_serializer = AllStudentResultSerializer(report, many=True)
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'All Student Subject Wise Report!',
                'data': data_serializer.data
            })

        except Exception as e:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': str(e)
            })

    if request.method == 'POST':
        try:
            # exam_name = request.data['exam_name']
            # rank = request.data['rank']
            # name = request.data['name']
            # board = request.data['board']
            # timestamp = request.data['timestamp']
            # score = request.data['score']
            # negative_marking = request.data['negative_marking']

            # report_ins = AllStudentResult(
            #     exam_name=exam_name,
            #     rank=rank,
            #     name=name,
            #     board=board,
            #     timestamp=timestamp,
            #     score=score,
            #     negative_marking=negative_marking
            # )

            payload = request.data
            data_serializer = AllStudentResultSerializer(data=payload,context={'request': request})
            if data_serializer.is_valid():
                data_serializer.save()
                return Response({
                    'code': status.HTTP_200_OK,
                    'message': 'Data Saved!!!!!!!!',
                    'data': data_serializer.data

                })
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'All Student Subject Wise Report!',
            })

        except Exception as e:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': str(e)
            })


