from django.db import models
from django.db import models

class principal(models.Model):
    name=models.CharField(max_length=25)
    adress=models.CharField(max_length=30)
    email=models.EmailField()

class teachers(models.Model):
    name=models.CharField(max_length=26)
    adress=models.CharField(max_length=30)
    materials=models.CharField(principal,on_delete=models.CASCADE,primary_key=True)
    
class students(models.Model):
    id=models.IntegerField()
    name=models.CharField(max_length=40)
    price=models.FloatField(max_length=50)
    company=models.CharField(teachers,on_delete=models.CASCADE,primary_key=True)

# Create your models here.
