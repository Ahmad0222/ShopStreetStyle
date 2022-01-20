from django.urls import path

from Shop import views

urlpatterns = [
    path('checkout', views.checkout, name="checkout"),
    path('order-confirmed', views.order, name="order-confirmed")
]