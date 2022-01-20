import json
from django.http import JsonResponse
from django.core import serializers
from CMS.models import AvailableBrand, Spotlight
from django.shortcuts import render
from Products.models import Product

# Create your views here.


def product(request):
    product = Product.objects.all()
    brand = AvailableBrand.objects.all()
    spotlight = Spotlight.objects.all()
    return render(request, 'index.html', {'product': product, 'brands': brand, 'spotlight': spotlight})


def shoes_page(request):
    shoes = Product.objects.filter(category=1)
    return render(request, 'shoes.html', {'product': shoes})


def bags_page(request):
    bags = Product.objects.filter(category=2)
    return render(request, 'bags.html', {'product': bags})


def apperals_page(request):
    apperals = Product.objects.filter(category=3)
    return render(request, 'apparel.html', {'product': apperals})


def product_view(request, slug):
    context = Product.objects.get(slug=slug)
    return render(request, 'detail_product.html', {'context': context})


def product_page(request):
    products = Product.objects.all()
    pro = {"product": products}
    return render(request, 'product_card_detail.html', pro)