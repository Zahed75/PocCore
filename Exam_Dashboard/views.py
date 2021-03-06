import random
import string
from builtins import Exception

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from Student_ExamDashboard.models import *
from .serializers import *


# create view here

# create Exma id
def generate_exam_id():
    s = 6
    global exam_id
    exam_id = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=s))
    exam_id = "#POC" + str(exam_id)
    # print(exam_id)
    return exam_id


# print(generate_exam_id(), "zahed")


# @api_view()
# def home(request):
#     return Response({'status': 200, 'message': "WELCOME TO POCEXAM TOOLS API HE HA HA..."})


class home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Exam_Dashboard/index.html'

    def get(self, request):
        queryset = {}
        return Response(queryset)


# add an exam
@api_view(['POST'])
@parser_classes([MultiPartParser])
def add_exam_pack(request):
    try:
        payload = request.data
        data_serializer = ExamPackSerializer(data=payload, context={'request': request})
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'Exam Pack Created Successfully!',
                'data': data_serializer.data
            })

        else:
            return Response(data_serializer.errors)
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


# edit exam pack

@api_view(['PUT'])
@parser_classes([MultiPartParser])
def Update_ExamPack(request, id):
    try:
        exam_obj = ExamPack.objects.get(id=id)
        Serializer = ExamPackSerializer(exam_obj, data=request.data, partial=True, context={'request': request})
        print(Serializer)
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


@api_view(['POST'])
@parser_classes([MultiPartParser])
def Create_Exam(request):
    try:
        # payload = request.data
        id_exam = generate_exam_id()
        request.data['exam_id'] = id_exam
        payload = request.data
        data_serializer = CreatExamSerializer(data=payload, context={'request': request})
        if data_serializer.is_valid():
            data_serializer.save()
            # print(payload)
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
@parser_classes([MultiPartParser])
def Update_CreateExam(request, id):
    try:
        Exam_obj = CreateExam.objects.get(id=id)
        Serializer = CreatExamSerializer(
            Exam_obj, data=request.data, partial=True)
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


@api_view(['DELETE'])
def delete_create_exam(request, id):
    try:
        exam_obj = CreateExam.objects.get(id=id)
        exam_obj.delete()
        return Response({'status': 202, 'message': 'Your Create Exam has Been Deleted!'})

    except Exception as e:
        print(e)
        return Response({'status': 403, 'message': 'invalid id'})


@api_view(['GET'])
def student_info(request):
    # stu_data=StudentProfile.objects.all()
    # for x in stu_data:
    #     print(x.user)
    try:
        stu_info = StudentProfile.objects.all()
        data_serializer = StudentProfileSerializer(stu_info, many=True, context={'request': request})

        return Response({

            'code': status.HTTP_200_OK,
            'message': 'List of all the Student!',
            'data': data_serializer.data,

        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


# =============================Question api start=========


@api_view(['POST'])
@parser_classes([MultiPartParser])
def create_q_one(request):
    try:
        payload = request.data
        data_serializer = CreateQuestionModelOneSerializer(data=payload, context={'request': request})
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'MCQ Type One Sent Successfully!',
                'data': data_serializer.data

            })
        else:
            return Response(data_serializer.errors)

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['POST'])
@parser_classes([MultiPartParser])
def create_q_two(request):
    try:
        payload = request.data
        data_serializer = CreateQuestionModelTwoSerializer(data=payload, context={'request': request})
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'MCQ Type One Sent Successfully!',
                'data': data_serializer.data

            })
        else:
            return Response(data_serializer.errors)

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['POST'])
@parser_classes([MultiPartParser])
def create_q_three(request):
    try:
        payload = request.data
        data_serializer = CreateQuestionModelThreeSerializer(data=payload, context={'request': request})
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'MCQ Type One Sent Successfully!',
                'data': data_serializer.data

            })
        else:
            return Response(data_serializer.errors)

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


# =========================Ans API=========


@api_view(['POST'])
@parser_classes([MultiPartParser])
def ans_type_one(request):
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


# @api_view(['POST'])
# @parser_classes([MultiPartParser])
# def ans_type_three(request):
#     try:
#         payload = request.data
#         data_seriazlier = CreateAnsThreeSerializer(data=payload)
#         if data_seriazlier.is_valid(raise_exception=True):
#             data_seriazlier.save()
#             return Response({
#                 'code': status.HTTP_200_OK,
#                 'message': 'Ans Has Been Set!!',
#                 'data': data_seriazlier.data
#             })
#         else:
#             return Response(
#                 data_seriazlier.errors
#             )
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'message': str(e)
#         })


@api_view(['GET'])
@parser_classes([MultiPartParser])
def GetStudentReport(request):
    print(request.user)
    try:
        # report_info = ExamResult.objects.filter(student=request.user)
        report_info = ExamResult.objects.all()
        data_serializer = ExamResultSerializer(report_info, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Student Report!',
            'data': data_serializer.data
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
@parser_classes([MultiPartParser])
def all_student_exam_report(request, exam_name):
    try:
        report = AllStudentResult.objects.filter(
            exam_name__Exam_name=exam_name)
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


@api_view(['DELETE'])
@parser_classes([MultiPartParser])
def QuestionOneDelete(request, id):
    try:
        q_one_obj = QuestionModel_One.objects.get(id=id)
        print(q_one_obj)
        q_one_obj.delete()

        return Response({'status': 202, 'mesaage': 'deleted'})

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['DELETE'])
@parser_classes([MultiPartParser])
def QuestionTwoDelete(request, id):
    try:
        q_one_obj = QuestionModel_Two.objects.get(id=id)
        print(q_one_obj)
        q_one_obj.delete()

        return Response({'status': 202, 'mesaage': 'deleted'})

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['DELETE'])
@parser_classes([MultiPartParser])
def QuestionThreeDelete(request, id):
    try:
        q_one_obj = QuestionModel_Two.objects.get(id=id)
        print(q_one_obj)
        q_one_obj.delete()

        return Response({'status': 202, 'mesaage': 'deleted'})

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['POST', 'GET'])
@parser_classes([MultiPartParser])
def batch_settings(request):
    try:
        payload = request.data
        data_serializer = CreateBatchSettings(data=payload)
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'Batch data Saved!',
                'data': data_serializer.data
            })


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
@parser_classes([MultiPartParser])
def batch_settingsGet(request):
    try:
        batch_info = BatchSettings.objects.all()
        data_serializer = CreateBatchSettings(batch_info, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'All Batch Data Get!!!!',
            'data': data_serializer.data
        })


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['DELETE'])
def delete_batch(request, id):
    try:
        batch = BatchSettings.objects.get(id=id)
        batch.delete()
        return Response({'status': 202,
                         'mesaage': 'Batch Successfully deleted'})


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
def get_ans_one(request):
    try:
        ans_model_one = AnswerModel_One.objects.all()
        data_serializer = Anstype_oneSerializer(ans_model_one, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'All Ans Shown from Ans Model One!!!!',
            'data': data_serializer.data
        })


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)

        })


@api_view(['GET'])
def get_ans_two(request):
    try:
        ans_model_one = AnsModel_Two.objects.all()
        data_serializer = CreateAnsTypeTwoSerializer(ans_model_one, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'All Ans Shown from Ans Model Two!!!!',
            'data': data_serializer.data
        })


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)

        })


# @api_view(['GET'])
# def get_ans_three(request):
#     try:
#         ans_model_one = AnsModel_Three.objects.all()
#         data_serializer = CreateAnsThreeSerializer(ans_model_one, many=True)
#         return Response({
#             'code': status.HTTP_200_OK,
#             'message': 'All Ans Shown from Ans Model Three!!!!',
#             'data': data_serializer.data
#         })
#
#
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'message': str(e)
#
#         })


@api_view(['GET'])
@parser_classes([MultiPartParser])
def get_admin_exam_list(request):
    try:
        exam_list = CreateExam.objects.all()
        print(exam_list)
        data_serializer = CreatExamSerializer(exam_list, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'List of all Exam of Admin Section',
            'data': data_serializer.data

        })


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['PUT'])
@parser_classes([MultiPartParser])
def edit_question_one(request, id):
    try:
        question_obj = QuestionModel_One.objects.get(id=id)
        Serializer = CreateQuestionModelOneSerializer(question_obj, partial=True, data=request.data,
                                                      context={'request': request})

        if not Serializer.is_valid():
            return Response({
                'status': 200, 'payload': Serializer.data, 'message': 'Something Went Wrong'

            })
        Serializer.save()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Question model One Updated Successfully!',
            'data': Serializer.data
        })


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['DELETE'])
def delete_question_one(request, id):
    try:
        question_obj = QuestionModel_One.objects.get(id=id)
        question_obj.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Question One Model Deleted Successfully!',

        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['PUT'])
@parser_classes([MultiPartParser])
def edit_ans_model_one(request, id):
    try:
        ans_model_obj = AnswerModel_One.objects.get(id=id)
        Serializer = Anstype_oneSerializer(ans_model_obj, data=request.data, partial=True)
        if not Serializer.is_valid():
            return Response({
                'status': 200, 'payload': Serializer.data, 'message': 'Something Went Wrong'

            })
        Serializer.save()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Ans Model Updated Successfully!',
            'data': Serializer.data
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
@parser_classes([MultiPartParser])
def get_student_info(request):
    try:
        stu_obj = UserInfo.objects.all()
        data_serializer = UserInfoSerializer(stu_obj, many=True, context={'request': request})

        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Students Information GET Successfully!',
            'data': data_serializer.data
        })

    except Exception as e:

        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['PUT'])
@parser_classes([MultiPartParser])
def edit_question_two(request, id):
    try:
        question_obj = QuestionModel_Two.objects.get(id=id)
        Serializer = CreateQuestionModelTwoSerializer(question_obj, partial=True, data=request.data,
                                                      context={'request': request})

        if not Serializer.is_valid():
            return Response({
                'status': 200, 'payload': Serializer.data, 'message': 'Something Went Wrong'

            })
        Serializer.save()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Question model One Updated Successfully!',
            'data': Serializer.data
        })


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['DELETE'])
def delete_question_two(request, id):
    try:
        question_obj = QuestionModel_Two.objects.get(id=id)
        question_obj.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Question Two Model Deleted Successfully!',

        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['PUT'])
@parser_classes([MultiPartParser])
def edit_ans_model_two(request, id):
    try:
        ans_model_obj = AnsModel_Two.objects.get(id=id)
        Serializer = CreateAnsTypeTwoSerializer(ans_model_obj, data=request.data, partial=True)
        if not Serializer.is_valid():
            return Response({
                'status': 200, 'payload': Serializer.data, 'message': 'Something Went Wrong'

            })
        Serializer.save()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Ans Model Updated Successfully!',
            'data': Serializer.data
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['PUT'])
@parser_classes([MultiPartParser])
def edit_question_three(request, id):
    try:
        question_obj = QuestionModel_Two.objects.get(id=id)
        Serializer = CreateQuestionModelThreeSerializer(question_obj, partial=True, data=request.data,
                                                        context={'request': request})

        if not Serializer.is_valid():
            return Response({
                'status': 200, 'payload': Serializer.data, 'message': 'Something Went Wrong'

            })
        Serializer.save()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Question model One Updated Successfully!',
            'data': Serializer.data
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['PUT'])
@parser_classes([MultiPartParser])
def edit_question_three(request, id):
    try:
        question_three = QuestionModel_Three.objects.get(id=id)
        Serializer = CreateQuestionModelThreeSerializer(question_three, data=request.data, partial=True)
        if not Serializer.is_valid():
            return Response({
                'status': 200, 'payload': Serializer.data, 'message': 'Something Went Wrong'

            })
        Serializer.save()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Question Model Updated Successfully!',
            'data': Serializer.data
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['DELETE'])
def delete_question_three(request, id):
    try:
        question_obj = QuestionModel_Three.objects.get(id=id)
        question_obj.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Question Three Model Deleted Successfully!',

        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['POST'])
@parser_classes([MultiPartParser])
def ans_sheet(request):
    try:
        payload = request.data.copy()
        payload['user'] = request.user.id
        print(payload)
        data_serializer = ViewAnsSheetSerializer(data=payload, context={'request': request})
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'All Question AnsSheet Get Down Successfully!',
                'data': data_serializer.data
            })
        else:
            return Response(data_serializer.errors)

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
@parser_classes([MultiPartParser])
def get_ans_sheet(request, exam_id):
    try:
        ans_sheet = ViewAnsSheet.objects.filter(user=request.user, exam_id=exam_id)
        print(ans_sheet)
        data_serializer = ViewAnsSheetSerializer(ans_sheet, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Ans Sheet Get Down!',
            'data': data_serializer.data
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })
