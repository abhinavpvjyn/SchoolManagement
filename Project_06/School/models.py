from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
class Studmark(models.Model):
    stdid=models.ForeignKey(Student,on_delete=models.CASCADE)
    mark=models.IntegerField()
    grade=models.CharField(max_length=10)
    
class User(AbstractUser):
    usertype=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    place=models.CharField(max_length=20)
    status=models.IntegerField()
    
