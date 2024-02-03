from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    username=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.username
    

# Create your models here.
