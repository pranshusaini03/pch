from django.db import models
class dgroomer(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50)
    shortaddress=models.CharField(max_length=500)
    address=models.TextField()
    phone_no=models.CharField(max_length=50)
    opening_Hours=models.CharField(max_length=50)
    
class lgroomer(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50)
    shortaddress=models.CharField(max_length=500)
    address=models.TextField()
    phone_no=models.CharField(max_length=50)
    opening_Hours=models.CharField(max_length=50)

class mgroomer(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50)
    shortaddress=models.CharField(max_length=500)
    address=models.TextField()
    phone_no=models.CharField(max_length=50)
    opening_Hours=models.CharField(max_length=50)

class bgroomer(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50)
    shortaddress=models.CharField(max_length=500)
    address=models.TextField()
    phone_no=models.CharField(max_length=50)
    opening_Hours=models.CharField(max_length=50)

class kgroomer(models.Model):
    image=models.URLField(max_length=200)
    name=models.CharField(max_length=50)
    shortaddress=models.CharField(max_length=500)
    address=models.TextField()
    phone_no=models.CharField(max_length=50)
    opening_Hours=models.CharField(max_length=50)

class hgroomer(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50)
    shortaddress=models.CharField(max_length=500)
    address=models.TextField()
    phone_no=models.CharField(max_length=50)
    opening_Hours=models.CharField(max_length=50)
# Create your models here.
