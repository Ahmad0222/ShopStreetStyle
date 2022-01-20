from django.urls import path
from django.contrib import admin
from CMS import views

#django admin customization start
admin.site.site_header = "Shop Street Style"
admin.site.index_title = "Welcome to Shop Street Style"
admin.site.site_title = "Shop Street Style"
#django admin customization end
urlpatterns = [
    path('account', views.Login, name="Login"),
    path('Login', views.handleLogin, name="handleLogin"),
    # path('Signup', views.signup, name= "signup"),
    path('signup/otp-confirmation', views.handleSignup, name="handleSignup"),
    path('signup/otp-confirmed', views.otp_call, name="otpCall"),
    path('signup/resend-otp', views.resend_otp, name='resend'),
    path('cart', views.cart, name='cart'),
]