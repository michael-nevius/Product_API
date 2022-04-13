from django.db import models

# Create your models here.
class Product(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    inventory_quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    url = models.CharField(max_length=255)