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
import h5py

# create view here

@api_view(['POST'])
# @authentication_classes([])
# @permission_classes([])
def tokenObtainPair(request):
    try:
        payload = request.data
        login_serializer = LoginSerializer(data=payload)

        if login_serializer.is_valid():
            phone_number = login_serializer.validated_data.get('phone_number')
            password = login_serializer.validated_data.get('password')

            user_instance = User.objects.get(username=phone_number, is_active=True)

            if check_password(password, user_instance.password):
                refresh = RefreshToken.for_user(user_instance)

                return Response({
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh),
                    'token_type': str(refresh.payload['token_type']),
                    'expiry': refresh.payload['exp'],
                    'user_id': refresh.payload['user_id']
                })
            else:
                return Response({
                    "code": status.HTTP_401_UNAUTHORIZED,
                    "message": "No active account found with the given credentials",
                    "status_code": 401,
                    "errors": [
                        {
                            "status_code": 401,
                            "message": "No active account found with the given credentials"
                        }
                    ]
                })
        else:
            return Response(login_serializer.errors)
    except Exception as e:
        return Response({
            "code": status.HTTP_401_UNAUTHORIZED,
            "message": str(e),
            "status_code": 401,
            "errors": [
                {
                    "status_code": 401,
                    "message": str(e)
                }
            ]
        })


@api_view(['POST'])
def tokenRefresh(request):
    try:
        payload = request.data
        refresh = RefreshToken(token=payload.get('refresh_token'), verify=True)

        return Response({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'token_type': str(refresh.payload['token_type']),
            'expiry': refresh.payload['exp'],
            'user_id': refresh.payload['user_id']
        })
    except Exception as e:
        return Response({
            "code": status.HTTP_401_UNAUTHORIZED,
            "message": str(e),
            "status_code": 401,
            "errors": [
                {
                    "status_code": 401,
                    "message": str(e)
                }
            ]
        })


@api_view(['POST'])
def tokenVerify(request):
    try:
        payload = request.data
        verify = UntypedToken(token=payload.get('access_token'))

        return Response({
            'access_token': str(verify.token),
            'token_type': str(verify.payload['token_type']),
            'expiry': verify.payload['exp'],
            'user_id': verify.payload['user_id'],
        })
    except Exception as e:
        return Response({
            "code": status.HTTP_401_UNAUTHORIZED,
            "message": str(e),
            "status_code": 401,
            "errors": [
                {
                    "status_code": 401,
                    "message": str(e)
                }
            ]
        })


@api_view(['POST'])
def userRegister(request):
    try:
        payload = request.data
        data_serializer = RegistrationDataSerializer(data=payload)
        if data_serializer.is_valid():
            user_instance = User.objects.create(
                username=data_serializer.data.get('phone_number')
            )
            user_instance.set_password(data_serializer.data.get('password'))

            if request.data['staff']:
                group = Group.objects.get(name="Staff")
                group.user_set.add(user_instance)
                user_instance.is_staff = True

            user_instance.save()
            UserInfo.objects.create(
                user=user_instance,
                phone_number=data_serializer.data.get('phone_number')
            )
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'User created successfully!',
                'data': data_serializer.data
            })
        else:
            return Response(data_serializer.errors)



    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_logout(request):
    request.user.auth_token.delete()

    logout(request)

    return Response('User Logged out successfully')


@api_view(['POST'])
@parser_classes([MultiPartParser])
def Register(request):
    try:
        payload = request.data
        payload['user'] = request.user.id
        print(payload)
        data_serializer = StudentProfileSerializer(data=payload)
        print(data_serializer, "tst")
        if data_serializer.is_valid():
            data_serializer.save()
            print(data_serializer)

            return Response({
                'code': status.HTTP_200_OK,
                'message': 'StudentProfile created successfully!',
                'data': data_serializer.data
            })
        else:
            return Response(data_serializer.errors)


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['PUT'])
@parser_classes([MultiPartParser])
def update_student(request, id):
    try:
        student_object = StudentProfile.objects.get(id=id)
        print(f'test {student_object}')
        serializer = StudentProfileSerializer(student_object, data=request.data, partial=True)
        if not serializer.is_valid(raise_exception=True):
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something wnent wrong'})

        serializer.save()

        return Response({'status': 200, 'payload': serializer.data, 'message': 'data saved'})

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })
