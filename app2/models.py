from django.db import models

# Create your models here.

class books(models.Model):
    name = models.CharField(max_length=10)
    price = models.PositiveIntegerField()
    num = models.PositiveIntegerField()







