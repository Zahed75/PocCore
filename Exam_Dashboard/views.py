from builtins import Exception
from django.contrib.auth import login
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework import status
from rest_framework.serializers import Serializer

from .models import *

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.utils import json
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken, UntypedToken, Token
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
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


# create view here


# add an exam
@api_view(['POST'])
def add_exam_pack(request):
    try:
        payload = request.data
        data_seriazlier = ExamPackSerializer(data=payload)
        if data_seriazlier.is_valid():
            data_seriazlier.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'Exam Pack Created Successfully!',
                'data': data_seriazlier.data
            })

        else:
            return Response(data_seriazlier.errors)

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


# edit exam pack

@api_view(['PUT'])
def Update_ExamPack(request, id):
    try:
        exam_obj = ExamPack.objects.get(id=id)
        Serializer = ExamPackSerializer(exam_obj, data=request.data, partial=True)
        if not Serializer.is_valid():
            print(Serializer.errors)
            return Response({'status': 200, 'payload': Serializer.data, 'message': 'Something Went Wrong'})

        Serializer.save()
        return Response({'status': 200, 'payload': Serializer.data, 'message': 'Your Exam Pack Data Updated'})

    except Exception as e:
        print(e)
        return Response({'status': 403, 'message': 'invalid id'})
