from django.db import models

class Categories(models.Model):
    food = models.CharField(max_length=256)
    clothes = models.CharField(max_length=256)
    electronic = models.CharField(max_length=256)
    for_home = models.CharField(max_length=256)
    car = models.CharField(max_length=256)
    mobile = models.CharField(max_length=256)
    apartment = models.CharField(max_length=256)
    travelling = models.CharField(max_length=256)
    medical = models.CharField(max_length=256)
    gifts = models.CharField(max_length=256)
    transfer = models.CharField(max_length=256)
    saves = models.CharField(max_length=256)
