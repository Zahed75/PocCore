from django.conf.urls import url
from django.urls import path
from Student_ExamDashboard.views import *


urlpatterns = [
    path('api/get_exam_pack/',get_exam_pack),
    path('api/exam_list/',ExamList),
    path('api/get_question/<int:exam_id>/',get_question),
    # path('api/ans_validation/<str:question_name>',ans_validation),
    path('api/ans_validation/',ans_validation),
    path('api/get_report/',get_report),
    path('api/get_all_student_sub/<str:exam_name>',all_student_result),


]
