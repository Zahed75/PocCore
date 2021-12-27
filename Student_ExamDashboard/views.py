from django.shortcuts import render
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
def question_set(request):
    try:
        pass




    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })
