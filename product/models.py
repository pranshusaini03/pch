from django.db import models
class products(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    message=models.TextField()
    pet=models.CharField(max_length=50)
    type1=models.CharField(max_length=50)
# Create your models here.
