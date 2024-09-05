from django.db import models

# Create your models here.
class Student(models.Model):
    rollno=models.IntegerField(primary_key=True)
    stuname=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    year=models.CharField(max_length=30)