from django.conf.urls import url
from django.urls import path
from Student_ExamDashboard.views import *


urlpatterns = [
    path('api/get_exam_pack/',get_exam_pack),
    path('api/exam_list/',ExamList),
    path('api/get_question/<int:exam_id>/',get_question),

]
