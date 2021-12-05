from django.conf.urls import url
from django.urls import path
from Login_App.views import *

urlpatterns = [
    path('api/token/', tokenObtainPair),
    path('api/token/refresh/', tokenRefresh),
    path('api/token/verify/', tokenVerify),
    path('api/register/', userRegister),
    path('api/student_profile/',StudentProfile),
]
