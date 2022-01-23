from django.db import models
from django.contrib.auth.models import User
import base64


# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_phone')
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return self.phone_number


class StudentProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Profile_image = models.ImageField(upload_to='Student_Profile', blank=True, null=True)
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=40, blank=True, null=True)
    level = models.CharField(max_length=60, blank=False, verbose_name='Student level')
    batch = models.CharField(max_length=70, blank=False)
    board = models.CharField(max_length=80, blank=False)
    institution = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return str(self.user)
