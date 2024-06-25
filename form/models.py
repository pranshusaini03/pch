from django.db import models
class form(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    pettype=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    
class groomingform(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    pettype=models.CharField(max_length=100)
    date=models.DateField(max_length=100)
    time=models.TimeField()
    
class healthform(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    pettype=models.CharField(max_length=100)
    date=models.DateField(max_length=100)
    time=models.TimeField()
    message=models.CharField(max_length=100)      
# Create your models here.
