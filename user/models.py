from django.db import models

from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=500)
    email = models.EmailField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)

    # def __str__(self):
    #     return self.name
