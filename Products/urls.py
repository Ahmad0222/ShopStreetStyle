from django.urls import path
from django.conf import settings
from Products import views

urlpatterns = [
    path('', views.product, name="product"),
    path('products', views.product_page, name="products"),
    path('shoes', views.shoes_page, name="shoes"),
    path('bags&accessories', views.bags_page, name="bags"),
    path('apperals', views.apperals_page, name="apperals"),
    path("products/<slug:slug>", views.product_view, name="detail_view"),
]