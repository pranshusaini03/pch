from django.db import models
class cart(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    message=models.TextField()