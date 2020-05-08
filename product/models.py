from django.db import models
''' Endilega finna fleiri attributess'''
class Category(models.Model):
    name = models.CharField(max_length=255)

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

class Platform(models.Model):
    name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, default=1)

class Product(models.Model):
    name = models.CharField(max_length=255)
    releaseDate = models.DateTimeField()
<<<<<<< HEAD
=======
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
>>>>>>> 4cd8a7132e48ec955c5cb6c12052d73669559af0
    description = models.TextField()
    price = models.FloatField()
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.CharField(max_length=255)










