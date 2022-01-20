import json

from django.shortcuts import render
from .models import Order
from django.core.mail import EmailMessage
# Create your views here.

def checkout(request):
    return render(request, 'checkout.html')

def order(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        request.session['e_mail'] = email
        phone = request.POST.get('tel', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip_code', '')
        country = request.POST.get('country', '')
        order = Order(order=items_json, first_name=fname, last_name=lname, e_mail=email, phone=phone, street_address=address,
                      city=city, zip_code=zip_code, country=country)
        order.save()
        email = EmailMessage('Order from Shop', 'Order: ' + items_json + '\n' + 'Name: ' + fname + ' ' + lname + '\n' + 'Email: ' + email + '\n' + 'Phone: ' + phone + '\n' + 'Address: ' + address + '\n' + 'City: ' + city + '\n' + 'Zip Code: ' + zip_code + '\n' + 'Country: ' + country, to=['03164322144ahmad@gmail.com'])
        email.send()
        thank = True
        oid = str(order.order_id)
        e_mail = request.session['e_mail']
        email = EmailMessage('Order', 'Your order has been received. Your Order Id is '+ oid +' Thank you for shopping with us.', to=[e_mail])
        email.send()
        return render(request, 'checkout.html', {'thank': thank, 'id': oid})
    return render(request, 'checkout.html')


