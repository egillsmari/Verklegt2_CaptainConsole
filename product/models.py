from django.db import models

''' model class for Category table '''
class Category(models.Model):
    name = models.CharField(max_length=255)


''' model class for Manufacturer table '''
class Manufacturer(models.Model):
    name = models.CharField(max_length=255)


''' model class for Platform table, linked to Manufacturer with foreign key '''
class Platform(models.Model):
    name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, default=1)


''' model class for Products table, linked to Platform and Category via foreign keys '''
class Product(models.Model):
    name = models.CharField(max_length=255)
    releaseDate = models.DateTimeField()
    description = models.TextField()
    price = models.FloatField()
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    condition = models.CharField(max_length=50)


''' model class for ProductImage, linked to Product with foreign key '''
class ProductImage(models.Model):
    productImage = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)











