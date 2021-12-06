from django.conf.urls import url
from django.urls import path
from Exam_Dashboard.views import *


urlpatterns = [
    path('api/create_exam/',Create_Exam),
    path('api/UpdateExamPack/<id>',UpdateExamPack,name='change_exam'),

]
