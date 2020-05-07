from django.db import models
''' Endilega finna fleiri attributess'''
class Category(models.Model):
    name = models.CharField(max_length=255)

class Platform(models.Model):
    name = models.CharField(max_length=30)

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    releaseDate = models.DateTimeField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField()
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.CharField(max_length=255)










