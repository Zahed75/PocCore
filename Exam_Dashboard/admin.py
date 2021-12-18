from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(ExamPack)
class ExamPackModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'ExamPack_name',
                    'details', 'batch', 'level')


@admin.register(CreateExam)
class CreateExamModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'Exam_name', 'details', 'time',
                    'date', 'batch', 'exam_pack', 'total_mark', 'pass_mark', 'amount_per_mistake', 'level')


# admin.site.register(Q_TypeOne)
# admin.site.register(Q_TypeTwo)
# admin.site.register(Q_TypeThree)
#
#
# class AnswerType_OneAdmin(admin.StackedInline):
#     model = AnswerType_One
#
#
# class Q_TypeOneAdmin(admin.ModelAdmin):
#     inlines = [AnswerType_One]
#
#
# admin.site.register(AnswerType_One)
# admin.site.register(AnswerType_Two)
# admin.site.register(AnswerType_Three)


class AnswerAdmin(admin.StackedInline):
    model = Answer
    fk_name = "Question"



class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]


admin.site.register(QuestionModel, QuestionAdmin)

admin.site.register(Answer)
