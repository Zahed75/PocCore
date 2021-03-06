from django.conf.urls import url
from django.urls import path
from Login_App.views import *

urlpatterns = [
    path('api/token/', tokenObtainPair),
    path('api/token/refresh/', tokenRefresh),
    path('api/token/verify/', tokenVerify),
    path('api/register/', userRegister),
    path('api/Student_Register/', Register),
    path('api/update_student/<id>', update_student, name='update'),
    path('api/LogOut/', User_logout),
    # path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_change/', Update_Password),
    path('api/admin_login/',admin_login),
    path('api/user_block/',block_user),
    path('api/delete_user/<username>',delete_user)
]
