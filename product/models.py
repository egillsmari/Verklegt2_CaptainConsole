from django.db import models
''' Endilega finna fleiri attributess'''
class Category(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    releaseDate = models.DateTimeField()
    type = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    platform = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.CharField(max_length=255)




