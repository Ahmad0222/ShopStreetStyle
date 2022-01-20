from django.db import models

# Create your models here.

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order = models.JSONField(max_length=5000)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    e_mail = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    street_address = models.CharField(max_length=300)
    city = models.CharField(max_length=30)
    zip_code = models.PositiveIntegerField()
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ["-order_id"]

