from django.conf.urls import url
from django.urls import path
from .models import *
from user.views import *
urlpatterns = [
    path('api/create_custom_user/', creatCustomUser)
]
