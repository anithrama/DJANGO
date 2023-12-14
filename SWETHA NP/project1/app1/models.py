from django.db import models

# Create your models here.
class student(models.Model):
    username=models.CharField(max_length=45)
    email=models.CharField(max_length=50)
    password=models.IntegerField()
    confirmpassword=models.IntegerField()
  
