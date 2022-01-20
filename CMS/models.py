from django.db import models
from Products.models import Category
# Create your models here.


class Banner(models.Model):
    type = models.CharField(max_length=20)
    heading = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    button_link = models.URLField(max_length=200)
    image = models.ImageField(upload_to="Banners")

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'


class AvailableBrand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Brands")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Available Brand'
        verbose_name_plural = 'Available Brands'



class FeaturedCollection(models.Model):
    category = models.ForeignKey('Products.Category', on_delete=models.CASCADE)
    productName = models.CharField(max_length=30)
    description = models.TextField(max_length=150)
    buttonLink = models.URLField(max_length=200)
    image = models.ImageField(upload_to="Featured Collections")

    def __str__(self):
        return self.productName

    class Meta:
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'

class Featured(models.Model):
    Description = models.TextField(max_length=250)
    collection = models.ManyToManyField(FeaturedCollection)
    def __str__(self):
        return "Featured Collections"
    class Meta:
        verbose_name = 'Featured Collection'
        verbose_name_plural = 'Featured Collections'

class Spotlight(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=500)
    image = models.ImageField(upload_to="Spotlight")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Spotlight'
        verbose_name_plural = 'Spotlight'

