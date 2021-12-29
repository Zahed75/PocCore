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
    Exam_start_time = models.TimeField()
    Exam_start_date = models.DateField()
    Exam_end_time = models.TimeField()
    Exam_end_date = models.DateField()

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


class Question_model_one(models.Model):
    exam_pack = models.ForeignKey(ExamPack, on_delete=models.CASCADE)
    exam_name = models.ForeignKey(CreateExam, on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='Question_img', null=True, blank=True)

    option_one = models.CharField(max_length=2000, null=True, blank=True)
    option_one_is_correct = models.BooleanField(default=False)

    option_two = models.CharField(max_length=2000, null=True, blank=True)
    option_two_is_correct = models.BooleanField(default=False)

    option_three = models.CharField(max_length=2000, null=True, blank=True)
    option_three_is_correct = models.BooleanField(default=False)

    option_four = models.CharField(max_length=2000, null=True, blank=True)
    option_four_is_correct = models.BooleanField(default=False)

    def __str__(self):
        return str(self.question)


class Question_model_two(models.Model):
    exam_pack = models.ForeignKey(ExamPack, on_delete=models.CASCADE)
    exam_name = models.ForeignKey(CreateExam, on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='Question_img', null=True, blank=True)

    data_one = models.CharField(max_length=2000, null=True, blank=True)
    data_two = models.CharField(max_length=2000, null=True, blank=True)
    data_three = models.CharField(max_length=2000, null=True, blank=True)

    option_one = models.CharField(max_length=2000, null=True, blank=True)
    option_one_is_correct = models.BooleanField(default=False)

    option_two = models.CharField(max_length=2000, null=True, blank=True)
    option_two_is_correct = models.BooleanField(default=False)

    option_three = models.CharField(max_length=2000, null=True, blank=True)
    option_three_is_correct = models.BooleanField(default=False)

    option_four = models.CharField(max_length=2000, null=True, blank=True)
    option_four_is_correct = models.BooleanField(default=False)

    def __str__(self):
        return str(self.question)


class Question_model_three(models.Model):
    exam_pack = models.ForeignKey(ExamPack, on_delete=models.CASCADE)
    exam_name = models.ForeignKey(CreateExam, on_delete=models.CASCADE)
    paragraph = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='Question_img', null=True, blank=True)

    #     ----------- Model one style embeds here ----------------

    one_question = models.CharField(max_length=1000, null=True, blank=True)
    one_image = models.ImageField(upload_to='Question_img', null=True, blank=True)

    one_option_one = models.CharField(max_length=1000, null=True, blank=True)
    one_option_one_is_correct = models.BooleanField(default=False)

    one_option_two = models.CharField(max_length=1000, null=True, blank=True)
    one_option_two_is_correct = models.BooleanField(default=False)

    one_option_three = models.CharField(max_length=1000, null=True, blank=True)
    one_option_three_is_correct = models.BooleanField(default=False)

    one_option_four = models.CharField(max_length=1000, null=True, blank=True)
    one_option_four_is_correct = models.BooleanField(default=False)

    #     ----------- Model two style embeds here ----------------

    two_question = models.CharField(max_length=3000, null=True, blank=True)
    two_image = models.ImageField(upload_to='Question_img', null=True, blank=True)

    two_data_one = models.CharField(max_length=1000, null=True, blank=True)
    two_data_two = models.CharField(max_length=1000, null=True, blank=True)
    two_data_three = models.CharField(max_length=1000, null=True, blank=True)

    two_option_one = models.CharField(max_length=1000, null=True, blank=True)
    two_option_one_is_correct = models.BooleanField(default=False)

    two_option_two = models.CharField(max_length=1000, null=True, blank=True)
    two_option_two_is_correct = models.BooleanField(default=False)

    two_option_three = models.CharField(max_length=1000, null=True, blank=True)
    two_option_three_is_correct = models.BooleanField(default=False)

    two_option_four = models.CharField(max_length=1000, null=True, blank=True)
    two_option_four_is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.paragraph
