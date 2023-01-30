from django.shortcuts import render
from django.http import HttpResponse
from .models import Buyer
from django.core.mail import send_mail
from random import randrange
from django.conf import settings
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def faqs(request):
    return render(request, 'faqs.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def add_row(request):
    Buyer.objects.create(
        first_name = 'kiran',
        last_name = 'patel',
        email = 'kiran@gmail.com',
        password = 'tops@123',
        address = '201,society, road, surat',
        mobile = '9089786756',
        gender = 'male'
    )
    return HttpResponse('row create thai gai')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        try:
            Buyer.objects.get(email = request.POST['email'])
            return render(request, 'register.html', {'msg': 'Email Is Already registered!!'})
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
                return render(request, 'register.html', {'msg': 'Both Passwords do not match!!'})


def otp(request):
   
    if str(c_otp) == request.POST['u_otp']:
        Buyer.objects.create(
            first_name = user_data[0],
            last_name = user_data[1],
            email = user_data[2],
            password = user_data[3]
        )
        return render(request, 'register.html', {'msg': 'Account created successfully!!'})
    else:
        return render(request, 'otp.html', {'msg': 'Wrong OTP enter again!!'})