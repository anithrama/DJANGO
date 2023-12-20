from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=25)
    email=models.IntegerField()
    password=models.CharField(max_length=35)

class det(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    password=models.CharField(max_length=35)
