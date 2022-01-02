from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(ExamResult)
class ExamResultModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'student',
                    'exam_name', 'score', 'negative_marking', 'timestamp')


@admin.register(AllStudentResult)
class AllStudentResultModel(admin.ModelAdmin):
    list_display = ('id', 'rank', 'name','board','timestamp','score','negative_marking')
