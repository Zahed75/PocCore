from django.conf.urls import url
from django.urls import path
from Student_ExamDashboard.views import *

urlpatterns = [
    path('api/get_student_exam_pack/', get_exam_pack),
    path('api/student_exam_list/', ExamList),
    path('api/get_question/<int:exam_id>/', get_question),
    path('api/ans_validation/', ans_validation),
    path('api/show_all_report/', show_all_report),  # student result
    path('api/get_result_specific_sub/<str:exam_name>', all_student_result),
    path('api/all_option_get/', option_all_get),

]
