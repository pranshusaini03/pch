from django.db import models
class dadopt(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50)
    shortaddress=models.CharField(max_length=500)
    address=models.TextField()
    phone_no=models.CharField(max_length=50)
    opening_Hours=models.CharField(max_length=50)
    rating=models.CharField(max_length=50)

class ladopt(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50)
    shortaddress=models.CharField(max_length=500)
    address=models.TextField()
    phone_no=models.CharField(max_length=50)
    opening_Hours=models.CharField(max_length=50)
    rating=models.CharField(max_length=50)
class madopt(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50)
    shortaddress=models.CharField(max_length=500)
    address=models.TextField()
    phone_no=models.CharField(max_length=50)
    opening_Hours=models.CharField(max_length=50)
    rating=models.CharField(max_length=50)
class badopt(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50)
    shortaddress=models.CharField(max_length=500)
    address=models.TextField()
    phone_no=models.CharField(max_length=50)
    opening_Hours=models.CharField(max_length=50)
    rating=models.CharField(max_length=50)
class kadopt(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50)
    shortaddress=models.CharField(max_length=500)
    address=models.TextField()
    phone_no=models.CharField(max_length=50)
    opening_Hours=models.CharField(max_length=50)
    rating=models.CharField(max_length=50)
class hadopt(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50)
    shortaddress=models.CharField(max_length=500)
    address=models.TextField()
    phone_no=models.CharField(max_length=50)
    opening_Hours=models.CharField(max_length=50)
    rating=models.CharField(max_length=50)
# claeate your models here.
