from django.conf.urls import url
from django.urls import path
from Exam_Dashboard.views import *

urlpatterns = [
    path('', home),
    path('api/add_exampack/', add_exam_pack),
    path('api/edit-exampack/<id>', Update_ExamPack, name='change'),
    path('api/delete-exampack/<id>', delete_exampack, name='delete'),
    path('api/list_examPack/', exampack_list, name='list-exampack'),
    path('api/create-exam/', Create_Exam),
    path('api/update-create-exam/<id>', Update_CreateExam, name='update-create-exam'),
    path('api/delete-create-exam/<id>', delete_create_exam),
    path('api/quiz_type_one/', q_type_one),
    path('api/ans_type_one/', ans_q_type_one),
    path('api/quize_type_two/', CreateQustion_two),
    path('api/ans_type_two/', ans_type_two),
    path('api/quizz_type_three/',create_question_three),
    path('api/ans_three/',ans_three),

]
