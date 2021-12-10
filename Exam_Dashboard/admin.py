from django.contrib import admin
from .models import *


# Register your models here.


# Register your models here.

@admin.register(ExamPack)
class ExamPackModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'ExamPack_name', 'details', 'batch','level')


@admin.register(CreateExam)
class CreateExamModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'Exam_name', 'details', 'time',
                    'date', 'batch', 'exam_pack', 'total_mark', 'pass_mark', 'amount_per_mistake','level')


@admin.register(Quiz)
class QuizModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam','question_body')
