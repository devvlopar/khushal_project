from django.shortcuts import render, redirect
from random import randrange
from django.conf import settings
from .models import *
from buyer.models import *
from django.core.mail import send_mail

# Create your views here.
def seller_index(request):
    #condition is given because we want to varify that seller has 
    # logged in or not
    try:
        s_obj = Seller.objects.get(email= request.session['seller_email'])

        return render(request, 'seller_index.html', {'seller_data':s_obj})
    except:
        return render(request, 'seller_login.html')


def seller_register(request):
    if request.method == 'GET':
        return render(request, 'seller_register.html')
    else:
        try:
            Buyer.objects.get(email = request.POST['email'])
            return render(request, 'seller_register.html', {'msg': 'Email Is Already registered!!'})
        except:
            if request.POST['password'] == request.POST['repassword']:
                s = "Ecommerce Registration!!"
                global user_data
                user_data = [request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password']]
                global c_otp
                c_otp = randrange(1000,9999)
                m = f'Hello User!!\nYour OTP is {c_otp}'
                f = settings.EMAIL_HOST_USER
                r = [request.POST['email']]
                send_mail(s, m, f, r)
                return render(request, 'otp.html', {'msg': 'Check Your MailBox'})
            else:
                return render(request, 'seller_register.html', {'msg': 'Both Passwords do not match!!'})


def seller_login(request):
    if request.method == 'POST':
        try:
            seller_obj = Seller.objects.get(email = request.POST['email'])
            if request.POST['password'] == seller_obj.password:
                request.session['seller_email'] = request.POST['email']
                return render(request, 'seller_index.html',{'seller_data': seller_obj})
            else:
                return render(request, 'seller_login.html', {'msg': 'Wrong Password!!'})

        except:
            return render(request, 'seller_login.html', {'msg':'Email is Not Registered!!'})

    else:
        return render(request, 'seller_login.html')


def seller_logout(request):
    del request.session['seller_email']
    return redirect('seller_login')    


def seller_edit_profile(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_edit_profile.html',{'seller_data': seller_obj})