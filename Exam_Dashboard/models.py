from django.db import models
from django.contrib.auth.models import User
from Login_App.models import *
import uuid

import base64


# Create your models here.


class ExamPack(models.Model):
    ExamPack_name = models.CharField(max_length=1000, verbose_name='Exam Pack Name')
    pack_image = models.ImageField(upload_to='pack_image', blank=True, null=True)
    details = models.TextField()
    batch = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.ExamPack_name


class CreateExam(models.Model):
    exam_pack = models.ForeignKey(ExamPack, on_delete=models.CASCADE, related_name='exam_pack')
    exam_id = models.CharField(max_length=40, blank=True)
    Exam_name = models.CharField(max_length=1000)
    details = models.TextField()
    Exam_start_time = models.CharField(max_length=60)
    Exam_start_date = models.DateField()
    Exam_end_time = models.CharField(max_length=60)
    Exam_end_date = models.DateField()
    exam_total_time = models.IntegerField(default=10)

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


class QuestionModel_One(models.Model):
    exam_pack = models.ForeignKey(ExamPack, on_delete=models.CASCADE)
    exam_name = models.ForeignKey(CreateExam, on_delete=models.CASCADE, related_name='name_of_exam')
    question_name = models.TextField(max_length=4000, blank=False, unique=True)
    q_image = models.ImageField(upload_to='Question_img', blank=True, null=True)
    marks = models.IntegerField(default=4)

    def __str__(self):
        return self.question_name


class AnswerModel_One(models.Model):
    Question = models.ForeignKey(QuestionModel_One, on_delete=models.CASCADE, related_name='Question')
    # Answer = models.CharField(max_length=3000)
    ans = models.CharField(max_length=3000)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.ans


class QuestionModel_Two(models.Model):
    exam_pack = models.ForeignKey(ExamPack, on_delete=models.CASCADE)
    exam_name = models.ForeignKey(CreateExam, on_delete=models.CASCADE, related_name='name_of_examTwo')
    description = models.TextField(max_length=4000, blank=True, null=True)
    question_name = models.TextField(max_length=4000, blank=True, null=True)
    Q_image = models.ImageField(upload_to='Question_img')
    data_one = models.CharField(max_length=3000, null=True, blank=True)
    data_two = models.CharField(max_length=3000, null=True, blank=True)
    data_three = models.CharField(max_length=3000, null=True, blank=True)
    marks = models.IntegerField(default=4)

    def __str__(self):
        return self.question_name


class AnsModel_Two(models.Model):
    Question = models.ForeignKey(QuestionModel_Two, on_delete=models.CASCADE, related_name='question_two')
    ans = models.CharField(max_length=400)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.ans


class QuestionModel_Three(models.Model):
    exam_pack = models.ForeignKey(ExamPack, on_delete=models.CASCADE)
    exam_name = models.ForeignKey(CreateExam, on_delete=models.CASCADE, related_name='name_of_examThree')
    Q_Description = models.TextField(max_length=5000)
    question_name = models.TextField(max_length=5000, null=True, blank=True)
    Q_image = models.ImageField(upload_to='Question_img', null=True, blank=True)
    # =========part_two======
    sample_one = models.CharField(max_length=400, null=True, blank=True)
    sample_two = models.CharField(max_length=400, null=True, blank=True)
    sample_three = models.CharField(max_length=400, null=True, blank=True)
    marks = models.IntegerField(default=4, null=True, blank=True)

    def __str__(self):
        return str(self.question_name)


class AnsModel_Three(models.Model):
    # Question_name = models.ForeignKey(QuestionModel_Three, on_delete=models.CASCADE, related_name='question_three')
    Question = models.ForeignKey(QuestionModel_Three, on_delete=models.CASCADE, related_name='question_three')
    ans = models.CharField(max_length=400)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.ans


class BatchSettings(models.Model):
    batch = models.CharField(max_length=599, blank=True, null=True)
    level = models.CharField(max_length=500, blank=True, null=True)
    board = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.batch)
