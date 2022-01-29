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


@admin.register(BatchSettings)
class BatchSettingsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'batch', 'level', 'board')


# class AnswerAdmin(admin.StackedInline):
#     model = AnswerModel_One
#     fk_name = "Question"
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [AnswerAdmin]
#
#
# admin.site.register(QuestionModel_One, QuestionAdmin)
#
# admin.site.register(AnswerModel_One)
#
#
# # ==========type 2nd===========start
#
# class AnswerAdmin(admin.StackedInline):
#     model = AnsModel_Two
#     # fk_name = "Question"
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [AnswerAdmin]
#
#

# admin.site.register(QuestionModel_Two, QuestionAdmin)
#
# admin.site.register(AnsModel_Two)
#
#
# # ============end==========
#
#
# # ============3rd question and ans model start====
#
# # class AnswerAdmin(admin.StackedInline):
# #     model = AnsModel_Three
#     # fk_name = "Question_name"
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [AnswerAdmin]
#
#
# # admin.site.register(QuestionModel_Three, QuestionAdmin)
# admin.site.register(QuestionAdmin)
#
# # admin.site.register(AnsModel_Three)
#
# # ============End
#
#
# admin.site.register(BatchSettings)

# admin.site.register(QuestionModel_One)

@admin.register(QuestionModel_One)
class QuestionModel_OneModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam_pack', 'exam_name', 'question_name', 'marks')


@admin.register(QuestionModel_Two)
class QuestionModel_TwoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam_pack', 'exam_name',
                    'question_name', 'description', 'data_one',
                    'data_two', 'data_three', 'data_four')


@admin.register(AnswerModel_One)
class AnswerModel_OneModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'Question', 'ans', 'is_correct')


admin.site.register(QuestionModel_Three)
admin.site.register(AnsModel_Two)
admin.site.register(AnsModel_Three)
admin.site.register(QuestionModel_Three_Sub)
admin.site.register(AnsModel_Three_Sub)
