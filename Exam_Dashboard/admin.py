from django.contrib import admin
from .models import *


# Register your models here.


# Register your models here.

@admin.register(ExamPack)
class ExamPackModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'ExamPack_name', 'details', 'batch',)


@admin.register(CreateExam)
class CreateExamModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'ExamPack_name', 'details', 'time',
                    'date', 'batch', 'exam_pack', 'total_mark', 'pass_mark', 'amount_per_mistake')
