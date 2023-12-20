from django.db import models

# Create your models here.

class Employee(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=25)
    designation=models.CharField(max_length=45)
    salary=models.IntegerField()
    place=models.CharField(max_length=45)
