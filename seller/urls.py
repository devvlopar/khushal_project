from .views import *
from django.urls import path

urlpatterns = [ 
    path('', seller_index, name='seller_index'),
    path('seller_register/', seller_register, name='seller_register')
]