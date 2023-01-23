from django.shortcuts import render
from django.http import HttpResponse
from .models import Buyer
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