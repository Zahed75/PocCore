from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(ExamPack)
class ExamPackModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'ExamPack_name',
                    'details', 'batch', 'level')


@admin.register(CreateExam)
class CreateExamModelAdmin(admin.ModelAdmin):
    list_display = ('id','exam_id', 'Exam_name', 'details',
                    'batch', 'exam_pack',
                    'Exam_start_time', 'total_mark',
                    'pass_mark', 'amount_per_mistake',
                    'level', 'Exam_start_date', 'Exam_end_time', 'Exam_end_date')


# ====question and ans model start=========


class AnswerAdmin(admin.StackedInline):
    model = AnswerMode_One
    fk_name = "Question"


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]


admin.site.register(QuestionModel_One, QuestionAdmin)

admin.site.register(AnswerMode_One)


# ==========type 2nd===========start

class AnswerAdmin(admin.StackedInline):
    model = AnsModel_Two
    fk_name = "Question"


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]


admin.site.register(QuestionModel_Two, QuestionAdmin)

admin.site.register(AnsModel_Two)


# ============end==========


# ============3rd question and ans model start====

class AnswerAdmin(admin.StackedInline):
    model = AnsModel_Three
    fk_name = "Question_name"


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]


admin.site.register(QuesionModel_Three, QuestionAdmin)

admin.site.register(AnsModel_Three)

# ============End
