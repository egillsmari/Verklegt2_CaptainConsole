from django.db import models

'''Create tables for products'''
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
    description = models.TextField()
    price = models.FloatField()
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    condition = models.CharField(max_length=50)

class ProductImage(models.Model):
    productImage = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)











