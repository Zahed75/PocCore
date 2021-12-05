from builtins import Exception
from django.contrib.auth import login
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework import status
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
from rest_framework.parsers import MultiPartParser, FormParser


# create view here







@api_view(['POST'])
def Create_Exam(request, format=None):
    try:
        payload = request.data['file']
        data_serializer = ExamPackSerializer(data=payload)
        if data_serializer.is_valid():
            exam_instance = ExamPack.objects.create(
                image=data_serializer.data.get('cover_photo')
            )
            exam_instance.save()
            ExamPack, object.create(
                exam=exam_instance,
                image=data_serializer.data.get('cover_photo')
            )


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })

# class ExamListView(APIView):
#     # parser_classes = (FormParser, MultiPartParser)
#     # @permission_classes([IsAuthenticated])
#
#     def post(self, request, format=None):
#         serializer = ExamPackSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save(
#                 photo=request.data.get('photo')
#             )
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
