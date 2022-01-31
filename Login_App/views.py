from builtins import Exception
from django.contrib.auth import login
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import UpdateAPIView
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
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# create view here

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def tokenObtainPair(request):
    try:
        payload = request.data
        login_serializer = LoginSerializer(data=payload)

        if login_serializer.is_valid():
            phone_number = login_serializer.validated_data.get('phone_number')
            password = login_serializer.validated_data.get('password')
            user_instance = User.objects.get(username=phone_number, is_active=True)
            user_info = UserInfo.objects.get(user=user_instance)
            print(user_info.is_block)
            # print(user_instance.is_superuser)
            # print(user_instance.is_staff)
            # print(user_instance.is_active)

            if check_password(password, user_instance.password):
                if not user_info.is_block:
                    refresh = RefreshToken.for_user(user_instance)
                else:
                    return Response({
                        "message": "Sorry You Are Blocked!"
                    })

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
        print(payload)
        data_serializer = RegistrationDataSerializer(data=payload)
        if data_serializer.is_valid():
            user_instance = User.objects.create(
                username=data_serializer.data.get('phone_number')
            )
            user_instance.set_password(data_serializer.data.get('password'))

            # if request.data['staff']:
            #     group = Group.objects.get(name="Staff")
            #     group.user_set.add(user_instance)
            #     user_instance.is_staff = True

            # if request.data['admin']:
            #     # group = Group.objects.get(name="Staff")
            #     # group.user_set.add(user_instance)
            #     user_instance.is_superuser=True

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
@parser_classes([MultiPartParser, FileUploadParser])
def Register(request):
    try:
        payload = request.data.copy()
        payload['user'] = request.user.id
        print(payload)
        data_serializer = StudentProfileSerializer(data=payload, context={'request': request})
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
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})

        serializer.save()

        return Response({'status': 200, 'payload': serializer.data, 'message': 'data saved'})

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


# @api_view(['PUT'])
# @parser_classes([MultiPartParser])
# def update_student(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         sinppet = ""
#         snippet = StudentProfile.objects.get(pk=pk)
#     except snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'PUT':
#         serializer = StudentProfileSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ChangePasswordView(generics.UpdateAPIView):
#     """
#     An endpoint for changing password.
#     """
#     serializer_class = ChangePasswordSerializer
#     model = UserInfo
#     permission_classes = (IsAuthenticated,)
#
#     def get_object(self, queryset=None):
#         obj = self.request.user
#         return obj
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)
#
#         if serializer.is_valid():
#             # Check old password
#             if not self.object.check_phone(serializer.data.get("old_password")):
#                 return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
#             # set_password also hashes the password that the user will get
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             response = {
#                 'status': 'success',
#                 'code': status.HTTP_200_OK,
#                 'message': 'Password updated successfully',
#                 'data': []
#             }
#
#             return Response(response)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#


# @api_view(['POST'])
# def Update_Password(request):
#     user=request.user
#     print(user)
#     try:
#         serializer = PasswordChangeSerializer(context={'request': request}, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         request.user.set_password(serializer.validated_data['new_password'])
#         request.user.save()
#
#         return Response({
#             'code': status.HTTP_200_OK,
#             'message': 'Password changed successfully!',
#             'data': serializer.data,
#
#         })
#
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'message': str(e)
#         })
#
#


@api_view(['POST'])
@parser_classes([MultiPartParser])
def Update_Password(request):
    try:
        user = request.data['phone_number']
        new_pass = request.data['password']
        user_ins = User.objects.get(username=user)
        user_ins.set_password(new_pass)
        user_ins.save()

        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Password changed successfully!',
            # 'data': serializer.data,
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['POST'])
def admin_login(request):
    try:
        payload = request.data
        login_serializer = LoginSerializer(data=payload)

        if login_serializer.is_valid():
            phone_number = login_serializer.validated_data.get('phone_number')
            password = login_serializer.validated_data.get('password')

            user_instance = User.objects.get(username=phone_number, is_active=True)
            print(user_instance.is_superuser)
            print(user_instance.is_staff)
            print(user_instance.is_active)

            if check_password(password, user_instance.password):
                if user_instance.is_superuser:
                    refresh = RefreshToken.for_user(user_instance)
                else:
                    return Response({
                        "message": "You Dont have an Access!"
                    })

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



    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['POST'])
@parser_classes([MultiPartParser])
def block_user(request):
    try:
        phone_number = request.data['phone_number']
        block_status = request.data['block_status']
        user_instance = User.objects.get(username=phone_number, is_active=True)
        user_info = UserInfo.objects.get(user=user_instance)
        if block_status == 'True':
            user_info.is_block = True
            user_info.save()
            return Response({
                "message": "User Blocked!!"
            })

        elif block_status == 'False':
            user_info.is_block = False
            user_info.save()
            return Response({
                "message": "User Unblock"
            })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['DELETE'])
@parser_classes([MultiPartParser])
def delete_user(request, username):
    try:
        user = User.objects.filter(username=username)
        user.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'User Deleted Successfully!',

        })



    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })



#
# import requests
#
# url = "http://developer.muthofun.com/sms.php?username=PocTech&password=JMWpxWV5a@Xb&mobiles=01706758112&sms=test sms&uniccode=1"
#
# payload={'username': 'PocTech',
# 'password': 'JMWpxWV5a@Xb',
# 'mobiles': '01706758112',
# 'sms': 'Hello Test sms'}
# files=[
#
# ]
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload, files=files)
#
# print(response.text)