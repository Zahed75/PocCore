from django.db import models
from django.contrib.auth.models import User
from Login_App.models import *
import uuid


# Create your models here.


class ExamPack(models.Model):
    ExamPack_name = models.CharField(max_length=1000, verbose_name='Exam Pack Name')
    details = models.TextField()
    batch = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.ExamPack_name


class CreateExam(models.Model):
    exam_pack = models.ForeignKey(ExamPack, on_delete=models.CASCADE, related_name='exam_pack')
    Exam_name = models.CharField(max_length=1000)
    details = models.TextField()
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    cover_photo = models.ImageField(upload_to='exam_cover_photos', blank=True, null=True)

    # assign student
    level = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)

    # marking
    total_mark = models.IntegerField(default=0)
    pass_mark = models.IntegerField(default=0)
    mark_per_question = models.IntegerField(default=1)

    isRandomized = models.BooleanField(default=False, verbose_name='Randomization')
    isSorted = models.BooleanField(default=False, verbose_name='Sorting')

    # for negative marking
    isNegativeMarking = models.BooleanField(default=False, verbose_name='Negative Marking')
    amount_per_mistake = models.FloatField(default=0, verbose_name='Amount per mistake')

    def __str__(self):
        return self.Exam_name


# =============Question Model=====================
# class Q_TypeOne(BaseModel):
#     question_name = models.CharField(max_length=4000)
#     Q_img = models.ImageField(upload_to='question_img')
#     mark = models.IntegerField(default=5)
#
#     def __str__(self):
#         return self.question_name
#
#
# class Q_TypeTwo(BaseModel):
#     question_name = models.CharField(max_length=4000)
#     Q_img = models.ImageField(upload_to='question_img')
#     type_one = models.CharField(max_length=400)
#     type_two = models.CharField(max_length=400)
#     type_three = models.CharField(max_length=400)
#     mark = models.IntegerField(default=5)
#
#     def __str__(self):
#         return self.question_name
#
#
# class Q_TypeThree(BaseModel):
#     question_name = models.CharField(max_length=4000)
#     Q_img = models.ImageField(upload_to='question_img')
#     type_one = models.ForeignKey(Q_TypeOne, on_delete=models.CASCADE, blank=True, null=True)
#     type_two = models.ForeignKey(Q_TypeTwo, on_delete=models.CASCADE, blank=True, null=True)
#     mark = models.IntegerField(default=5)
#
#     def __str__(self):
#         return self.question_name


# ===================End=====================

# (=======Answer Model Start==============)
# class AnswerType_One(BaseModel):
#     Question_type = models.ForeignKey(Q_TypeOne, on_delete=models.CASCADE)
#     ans = models.CharField(max_length=500)
#     is_correct = models.BooleanField(default=False)
#
#
# class AnswerType_Two(BaseModel):
#     Question_type = models.ForeignKey(Q_TypeTwo, on_delete=models.CASCADE)
#     ans = models.CharField(max_length=500)
#     is_correct = models.BooleanField(default=False)
#
#
# class AnswerType_Three(BaseModel):
#     Question_type = models.ForeignKey(Q_TypeThree, on_delete=models.CASCADE)
#     ans = models.CharField(max_length=500)
#     is_correct = models.BooleanField(default=False)

# ==============End========================

#
# class BaseModel(models.Model):
#     UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)
#
#     class Meta:
#         abstract: True


class QuestionModel_One(models.Model):
    question_name = models.TextField(max_length=4000, blank=False, unique=True)
    q_image = models.ImageField(upload_to='Question_img', blank=True, null=True)
    marks = models.IntegerField(default=5)

    def __str__(self):
        return self.question_name


class AnswerMode_One(models.Model):
    Question = models.ForeignKey(QuestionModel_One, on_delete=models.CASCADE, related_name='Question')
    Answer = models.CharField(max_length=3000)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.Answer


class QuestionModel_Two(models.Model):
    description = models.TextField(max_length=4000, blank=True, null=True)
    Q_name = models.TextField(max_length=4000, blank=True, null=True)
    Q_image = models.ImageField(upload_to='Question_img')
    marks = models.IntegerField(default=5)

    def __str__(self):
        return self.Q_name


class AnsModel_Two(models.Model):
    Question = models.ForeignKey(QuestionModel_Two, on_delete=models.CASCADE, related_name='question_two')
    ans = models.CharField(max_length=400)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.ans


class QuesionModel_Three(models.Model):
    Q_Description = models.TextField(max_length=5000)
    Q_one = models.TextField(max_length=5000)
    Q_image = models.ImageField(upload_to='Question_img')
    # =========part_two======
    sample_one = models.CharField(max_length=400)
    sample_two = models.CharField(max_length=400)
    sample_three = models.CharField(max_length=400)
    marks = models.IntegerField(default=5)

    def __str__(self):
        return str(self.Q_one)


class AnsModel_Three(models.Model):
    Question_name = models.ForeignKey(QuesionModel_Three, on_delete=models.CASCADE, related_name='question_three')
    ans = models.CharField(max_length=400)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.ans
