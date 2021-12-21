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
from json import dumps, loads, JSONEncoder, JSONDecoder
from .models import CreateExam
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


# create view here


@api_view()
def home(request):
    return Response({'status': 200, 'message': "WELCOME TO POCEXAM TOOLS API HE HA HA..."})


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


# ///Delete ExamPack

@api_view(['DELETE'])
def delete_exampack(request, id):
    try:
        exm_obj = ExamPack.objects.get(id=id)
        exm_obj.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Exam Pack Deleted Successfully!',
            'data': Serializer.data
        })


    except Exception as e:
        print(e)
        return Response({'status': 403, 'message': 'invalid'})


# show all exam pack

@api_view(['GET'])
def exampack_list(request):
    try:
        exam_list = ExamPack.objects.all()
        data_serializer = ExamPackSerializer(exam_list, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'List Of All ExamPack!',
            'data': data_serializer.data
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


# @api_view(['POST'])
# @csrf_exempt
# @parser_classes([MultiPartParser])
# def Create_Exam(request):
#     try:
#         payload = request.data
#         payload['ExamPack'] = request.ExamPack.id
#         data_serializer = CreatExamSerializer(data=payload)
#         if data_serializer.is_valid():
#             data_serializer.save()
#             return Response({
#                 'code': status.HTTP_200_OK,
#                 'message': 'Exam Has Been Created !',
#                 'data': data_serializer.data
#             })
#
#         else:
#             return Response(data_serializer.errors)
#
#
#
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'message': str(e)
#         })
#

@api_view(['POST'])
@parser_classes([MultiPartParser])
def Create_Exam(request):
    try:
        payload = request.data
        data_serializer = CreatExamSerializer(data=payload)
        print("test", data_serializer)
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'Exam Created Successfully!',
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
def Update_CreateExam(request, id):
    try:
        Exam_obj = CreateExam.objects.get(id=id)
        Serializer = CreatExamSerializer(Exam_obj, data=request.data, partial=True)
        if not Serializer.is_valid():
            return Response({
                'status': 200, 'payload': Serializer.data, 'message': 'Something Went Wrong'
            })
        Serializer.save()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Created Exam Data Updated Successfully!',
            'data': Serializer.data
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


# @api_view(['DELETE'])
# def delete_create_exam(request, id):
#     try:
#         Exam_obj =CreateExam.objects.get(id=id)
#         Exam_obj.delete()
#         return Response({
#             'code': status.HTTP_200_OK,
#             'message': 'Exam Pack Deleted Successfully!',
#             'data': Serializer.data
#         })
#
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'message': str(e)
#         })


@api_view(['DELETE'])
def delete_create_exam(request, id):
    try:
        exam_obj = CreateExam.objects.get(id=id)
        exam_obj.delete()
        return Response({'status': 202, 'message': 'Your Create Exam has Been Deleted!'})

    except Exception as e:
        print(e)
        return Response({'status': 403, 'message': 'invalid id'})


@api_view(['POST'])
@csrf_exempt
@parser_classes([MultiPartParser])
def q_type_one(request):
    try:
        payload = request.data
        data_serializer = Question_OneSerializer(data=payload)
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'M.C.Q Question Create Successfully!',
                'data': data_serializer.data
            })
        else:
            return Response({
                data_serializer.errors
            })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['POST'])
@parser_classes([MultiPartParser])
def ans_q_type_one(request):
    try:
        payload = request.data
        # payload['QuestionModel_One'] =request.data
        # data_serializer = Anstype_oneSerializer(data=payload)
        data_serializer = Anstype_oneSerializer(data=payload)
        if data_serializer.is_valid(raise_exception=True):
            data_serializer.save()

            return Response({
                'code': status.HTTP_200_OK,
                'message': 'Ans Set SuccessFully !',
                'data': data_serializer.data
            })
        else:
            return Response({
                data_serializer.errors
            })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['POST'])
@parser_classes([MultiPartParser])
def CreateQustion_two(request):
    try:
        payload = request.data
        data_serializer = CreateQuestionSerializerTwo(data=payload)
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'M.C.Q Question Type Two Create Successfully!',
                'data': data_serializer.data
            })
        else:
            return Response({
                data_serializer.errors
            })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['POST'])
@parser_classes([MultiPartParser])
def ans_type_two(request):
    try:
        payload = request.data
        data_serializer = CreateAnsTypeTwoSerializer(data=payload)
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'Ans Set SuccessFully !',
                'data': data_serializer.data
            })
        else:
            return Response({
                data_serializer.errors
            })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['POST'])
@parser_classes([MultiPartParser])
def create_question_three(request):
    try:
        payload = request.data
        data_seriazlier = CreateQuestionThreSerializer(data=payload)
        if data_seriazlier.is_valid():
            data_seriazlier.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'M.C.Q Question Create Successfully!',
                'data': data_seriazlier.data
            })

        else:
            return Response({
                data_seriazlier.errors
            })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['POST'])
@parser_classes([MultiPartParser])
def ans_three(request):
    try:
        payload = request.data
        data_seriazlier = CreateAnsThreeSerializer(data=payload)
        if data_seriazlier.is_valid(raise_exception=True):
            data_seriazlier.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'Ans Has Been Set!!',
                'data': data_seriazlier.data
            })
        else:
            return Response(
                data_seriazlier.errors
            )
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })
