from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import math
import random
from django.core.mail import EmailMessage


# Create your views here.

def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def handleSignup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        request.session['fname'] = fname
        lname = request.POST['lname']
        request.session['lname'] = lname
        username = fname+"_"+lname
        request.session['username'] = username
        emailField = request.POST['email']
        request.session['emailField'] = emailField
        pass1 = request.POST['pass1']
        request.session['pass1'] = pass1
        pass2 = request.POST['pass2']
        otp = generateOTP()
        request.session['otp'] = otp

        if pass1 == pass2:
            email = EmailMessage('OTP',
                                 'Your OTP for the verification of Signup Account For Shop Street Style is {}'.format(otp), to=[emailField])
            email.send()
        else:
            messages.error(request, 'Both Passwords are not same')
            return render(request, 'login.html')
        return render(request, 'otp_recieve.html')

def resend_otp(request):
    otp = generateOTP()
    request.session['otp'] = otp
    emailField = request.session['emailField']
    email = EmailMessage('OTP',
                         'Your OTP for the verification of Signup Account For Shop Street Style is {}'.format(otp),
                         to=[emailField])
    email.send()
    return render(request, 'otp_recieve.html')

def otp_call(request):
    if request.method == 'POST':
        digit_1 = request.POST['digit-1']
        digit_2 = request.POST['digit-2']
        digit_3 = request.POST['digit-3']
        digit_4 = request.POST['digit-4']
        digit_5 = request.POST['digit-5']
        digit_6 = request.POST['digit-6']
        input_otp = digit_1+digit_2+digit_3+digit_4+digit_5+digit_6
        otp = request.session['otp']
        if input_otp == otp:
            un = request.session['username']
            ef = request.session['emailField']
            p1 = request.session['pass1']
            fn = request.session['fname']
            ln = request.session['lname']
            creatUser = User.objects.create_user(username=un, email=ef, password=p1)
            creatUser.first_name = fn
            creatUser.last_name = ln
            creatUser.save()
            user = authenticate(username=un, password=p1)
            login(request, user)
            messages.success(request, f'Thanks for registering. You are now logged in as {un}')
            return redirect('products')
def Login(request):
    return render(request, 'login.html')

def handleLogin(request):
        # getting post values
        if request.method == 'POST':
            loginusername = request.POST['loginusername']
            loginpassword = request.POST['loginpassword']

            # authenticating values
            user = authenticate(username=loginusername, password=loginpassword)
            if user is not None:
                login(request, user)
                return redirect('products')
            else:
                messages.error(request, 'Invalid Credentials, Please Try Again')
                return render(request, 'login.html', {})


def cart(request):
    return render(request, 'cart.html')
