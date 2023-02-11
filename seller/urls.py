from .views import *
from django.urls import path

urlpatterns = [ 
    path('', seller_index, name='seller_index'),
    path('seller_register/', seller_register, name='seller_register'),
    path('seller_login/', seller_login, name='seller_login'),
    path('seller_logout/', seller_logout, name='seller_logout'),
    path('seller_edit_profile/', seller_edit_profile, name='seller_edit_profile'),



]