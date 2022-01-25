from django.contrib import admin
from .models import Category, size, Product, stock
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'product_code', 'price')
    list_filter = ("category",)
    search_fields = ['name', 'product_code']

admin.site.register(Category)
admin.site.register(size)
admin.site.register(stock)
admin.site.register(Product, ProductAdmin)