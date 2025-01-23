
from django.db import models

# Create your models here.

class Pickup(models.Model):
    fullname=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    NoItems=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    class Meta:
        db_table="Pickup"