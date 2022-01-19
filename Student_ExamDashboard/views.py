from rest_framework import status
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from Login_App.serializers import *
from .serializers import *
from Exam_Dashboard.serializers import *


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
        data_serializer = CreatExamSerializer(queryset, many=True, context={'request': request})

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
        question_type_three_sub = CreateQuestionModelThreeSerializer_Sub(QuestionModel_Three_Sub.objects.filter(exam_name=exam_id), many=True)

        data_dict = {
            "data_one": question_type_one.data,
            "data_two": question_type_two.data,
            "data_three": question_type_three.data,
            "data_three_sub": question_type_three_sub.data,
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
        question_three_sub = QuestionModel_Three_Sub.objects.filter(question_name=question_name)

        # print(question_one)
        # print(question_two)
        # print(question_three)
        # print(question_three_sub)

        question = None
        question_id = None

        question_model_array = [question_one, question_two, question_three, question_three_sub]

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
        ans_three_sub = AnsModel_Three_Sub.objects.filter(Question__question_name=question_name)
        print(ans_three_sub)

        # print(ans_one)
        # print(ans_two)
        # print(ans_three)
        # print(ans_three_sub)

        ans_model_array = [ans_one, ans_two, ans_three, ans_three_sub]

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


@api_view(['POST', 'GET'])
@parser_classes([MultiPartParser])
@permission_classes([IsAuthenticated])
def show_all_report(request):
    # user = request.user
    # student = CreateExam.objects.filter()
    # print(student)
    if request.method == 'GET':
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

    if request.method == 'POST':
        try:
            payload = request.data.copy()
            payload['user'] = request.user.id
            print(payload)

            data_serializer = ExamResultSerializer(data=payload, context={'request': request})
            if data_serializer.is_valid():
                data_serializer.save()
                return Response({
                    'code': status.HTTP_200_OK,
                    'message': 'data sent successfully!',
                    'data': data_serializer.data
                })
            else:
                return Response(data_serializer.errors)


        except Exception as e:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': str(e)
            })




@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser])
@permission_classes([IsAuthenticated])
def all_student_result(request, exam_name):
    # if request.method == 'POST':
    #     try:
    #
    #         payload = request.data
    #         data_serializer = ExamResultSerializer(data=payload, context={'request': request})
    #         if data_serializer.is_valid():
    #             data_serializer.save()
    #             return Response({
    #                 'code': status.HTTP_200_OK,
    #                 'message': 'Data  pass!!!!!!!!',
    #                 'data': data_serializer.data,
    #
    #             })
    #         return Response({
    #             'code': status.HTTP_200_OK,
    #             'message': 'Report Shown!!',
    #         })
    #
    #     except Exception as e:
    #         return Response({
    #             'code': status.HTTP_400_BAD_REQUEST,
    #             'message': str(e)
    #         })

    if request.method == 'GET':
        try:

            report = AllStudentResult.objects.filter(exam_name__Exam_name=exam_name)
            print(report)
            # prfl = StudentProfile.objects.filter(user__studentprofile=request.user)
            # prfl = StudentProfile.objects.all()
            # print(prfl)
            # stu_serializer = StudentProfileSerializer(prfl, many=True)
            data_serializer = AllStudentResultSerializer(report, many=True, context={'request': request})
            return Response({
                'code': status.HTTP_200_OK,
                'message': 'All Student Subject Wise Report!',
                'data': data_serializer.data,
                # 'prfl': stu_serializer.data

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
            data_serializer = AllStudentResultSerializer(data=payload, context={'request': request})
            if data_serializer.is_valid():
                data_serializer.save()
                return Response({
                    'code': status.HTTP_200_OK,
                    'message': 'Data Saved!!!!!!!!',
                    'data': data_serializer.data,

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


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser])
def option_all_get(request):
    try:
        question_name = request.data['question_name']
        ans_one = Anstype_oneSerializer(AnswerModel_One.objects.filter(Question__question_name=question_name),
                                        many=True)
        print(f'1, {ans_one}')
        print(len(ans_one.data))
        ans_two = CreateAnsTypeTwoSerializer(AnsModel_Two.objects.filter(Question__question_name=question_name),
                                             many=True)
        print(f'2, {ans_two}')
        ans_three = CreateAnsThreeSerializer(AnsModel_Three.objects.filter(Question__question_name=question_name),
                                             many=True)
        print(f'3, {ans_three}')
        ans_three_sub = CreateAnsThreeSerializer_Sub(AnsModel_Three_Sub.objects.filter(Question__question_name=question_name),
                                             many=True)
        print(f'3, {ans_three_sub}')

        ans_model_array = [ans_one.data, ans_two.data, ans_three.data, ans_three_sub.data]
        # ans_model_array = [ans_one.data, ans_two.data]
        print(ans_model_array)

        answer = None

        for item in ans_model_array:
            if len(item) > 0:
                answer = item
            else:
                pass

        print(answer)

        return Response({
            'code': status.HTTP_200_OK,
            'message': 'all option fetched!!!!!!!!',
            'data': answer,

        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })
