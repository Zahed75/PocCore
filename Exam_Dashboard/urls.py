from django.conf.urls import url
from django.urls import path
from Exam_Dashboard.views import *

urlpatterns = [
    path('api/add_exampack/', add_exam_pack),
    path('api/edit-exampack/<id>',Update_ExamPack),

]
