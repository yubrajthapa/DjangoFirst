from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_lenght=100)
      name = models.CharField(max_lenght=100)

    price = models.IntegerField()
    desc = models.CharField(max_length=200)
      