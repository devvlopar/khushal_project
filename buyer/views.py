from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail
from random import randrange
from django.conf import settings
from seller.models import *
# Create your views here.

def index(request):
    all_pros = Product.objects.all()
    try:
        #jyare login karel hoy
        buyer_row = Buyer.objects.get(email = request.session['email'])
        return render(request, 'index.html', {'user_data':buyer_row, 'all_products':all_pros})
    except:
        #jyare login nathi karyu
        return render(request, 'index.html', {'all_products': all_pros})

def about(request):
    try:
        buyer_row = Buyer.objects.get(email = request.session['email'])
        return render(request, 'about.html', {'user_data': buyer_row})
    except:
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
            # Buyer.objects.get(email = request.POST['email'])
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

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            #email check thay che
            buyer_row = Buyer.objects.get(email = request.POST['email'])
            
            #password check thay chhe
            # request.POST['password'] ###aa password tame login page ma enter karyo hase
            # buyer_row.password ###aa password database wado chhe
            if request.POST['password'] == buyer_row.password:
                #password sacho enter karyo chhe
                request.session['email'] = request.POST['email'] #login thai gayu/ session naam na glass ma email(je login na page par enter karyo hato e) mukaai gayo
                return redirect('index')
            else:
                return render(request, 'login.html', {'msg': 'Wrong Password!!'})
            
        except:
            #jyare email madyo nathi
            return render(request, 'login.html',{'msg':'email is not registered!!'})


def logout(request):
    # session mathi email kadhvano code 
    del request.session['email']

    # ab yahan se index funciton ki jawab daari hai
    return redirect('index')


def cart(request):
    u1 = Buyer.objects.get(email = request.session['email'])
    c_list = Cart.objects.filter(buyer = u1)
    t_amount = 0
    for i in c_list:
        t_amount += i.price
    
    return render(request, 'cart.html' , {'user_data':u1, 'my_cart_data': c_list, 'total_amount':t_amount})


def add_to_cart(request, pk):
    p_obj = Product.objects.get(id = pk)
    b1 = Buyer.objects.get(email = request.session['email'])
    Cart.objects.create(
        product_name = p_obj.product_name,
        price = p_obj.price,
        pic = p_obj.pic,
        buyer = b1
    )
    return redirect('index')


def del_cart_item(request, c_item):
    c_obj = Cart.objects.get(id = c_item)
    c_obj.delete()
    return redirect('cart')