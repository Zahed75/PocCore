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


# class BaseModel(models.Model):
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)


