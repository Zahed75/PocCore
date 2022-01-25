from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(UserInfo)
class UserInfoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number','is_block')


@admin.register(StudentProfile)
class StudentProfileModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'email', 'level', 'batch', 'board', 'institution')
