from django.db import models
from django.contrib.auth.models import User
from Exam_Dashboard.models import *
from Login_App.models import *


# Create your models here.

class ExamResult(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_result')
    exam_name = models.ForeignKey(CreateExam, on_delete=models.CASCADE, related_name='exam_result')
    score = models.CharField(max_length=500,blank=True,null=True)
    negative_marking = models.CharField(max_length=40,blank=True)
    timestamp = models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return self.student.username


class AllStudentResult(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_name = models.ForeignKey(CreateExam, on_delete=models.CASCADE)
    rank = models.CharField(max_length=400, null=True, blank=True)
    name = models.CharField(max_length=550, null=True, blank=True)
    board = models.CharField(max_length=550, null=True, blank=True)
    timestamp = models.CharField(max_length=550, null=True, blank=True)
    score = models.CharField(max_length=550, null=True, blank=True)
    negative_marking = models.CharField(max_length=550, null=True, blank=True)

    def __str__(self):
        return self.name
