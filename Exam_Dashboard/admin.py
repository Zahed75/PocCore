from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(ExamPack)
class ExamPackModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'ExamPack_name',
                    'details', 'batch', 'level')


@admin.register(CreateExam)
class CreateExamModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam_id', 'Exam_name', 'details',
                    'batch', 'exam_pack',
                    'Exam_start_time', 'total_mark',
                    'pass_mark', 'amount_per_mistake',
                    'level', 'Exam_start_date', 'Exam_end_time', 'Exam_end_date')


# ====question and ans model start=========


# @admin.register(AnswerMode_One)
# class AnswerMode_OneModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'Answer', 'is_correct')
#
#
# @admin.register(QuestionModel_One)
# class QuestionModel_OneModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'exam_pack', 'exam_name',
#                     'question_name', 'q_image', 'marks', 'answer')
#
#
# @admin.register(AnsModel_Two)
# class AnsModel_TwoModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'ans', 'is_correct')
#
#
# @admin.register(QuestionModel_Two)
# class QuestionModel_TwoModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'exam_pack', 'exam_name','Q_name','Q_image', 'marks', 'answer')
#
#
# @admin.register(AnsModel_Three)
# class AnsModel_ThreeModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'ans', 'is_correct')
#
#
# @admin.register(QuesionModel_Three)
# class QuesionModel_ThreeModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'exam_pack', 'exam_name',
#                     'Q_one', 'Q_image', 'marks', 'answer')


@admin.register(Question_model_one)
class Question_model_one_Admin(admin.ModelAdmin):
    list_display = ['id', 'question']

@admin.register(Question_model_two)
class Question_model_two_Admin(admin.ModelAdmin):
    list_display = ['id', 'question']

@admin.register(Question_model_three)
class Question_model_three_Admin(admin.ModelAdmin):
    list_display = ['id', 'paragraph']