from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    price = models.FloatField()
    unit = models.CharField(max_length=100)