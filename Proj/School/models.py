from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(AbstractUser):
#     usertype=models.CharField(max_length=20)
#     phone=models.CharField(max_length=20)
#     status=models.IntegerField()
class User(AbstractUser):
    usertype=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    status=models.CharField(max_length=10)
