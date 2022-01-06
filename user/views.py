from django.shortcuts import render
from builtins import Exception
from django.contrib.auth import login
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken, UntypedToken, Token
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model, logout
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser
from user.models import *
from django.contrib.auth.models import Group


@api_view(['POST'])
# @parser_classes([MultiPartParser])
def creatCustomUser(request):
    try:

        payload = request.data
        data_serializer = CreateCustomSerializer(data=payload)
        if data_serializer.is_valid():
            user_instance = CustomUser.objects.create(
                email=request.data['email']
            )
            user_instance.password(data_serializer.data.get('password'))

            if request.data['Staff']:
                group = Group.objects.get(name='Staff')
                user_instance.groups.add(group)
                print("Staff created")
            elif request.data['Admin']:
                group = Group.objects.get(name='Admin')
                user_instance.groups.add(group)
                print("Admin created")

            user_instance.save()

            CustomUser.objects.create(
                user=user_instance,
                email=data_serializer.data.get('email')
            )

        return Response({
            'code': status.HTTP_200_OK,
            'message': 'User created successfully!',
            'data': data_serializer.data
        })


    except Exception as e:

        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })
