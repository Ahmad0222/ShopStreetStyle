from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class size(models.Model):
    foot_size = models.IntegerField()

    def __str__(self):
        return str(self.foot_size)


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250)
    description = models.TextField(max_length=500)
    note = models.TextField(max_length=250)
    product_code = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    sizes = models.ManyToManyField(size, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='Products')
    best_selling = models.BooleanField(default=False)
    new_arrival = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ["-id"]



