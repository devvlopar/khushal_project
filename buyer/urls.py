from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('faqs/', faqs, name='faqs'),
    path('privacy/', privacy, name="privacy"),
    path('term/', terms , name="terms"),
    path('add_row/', add_row, name="add_row")
    

   
]



#html : structure
#css : styles/ looks
#JS : animation,responsiveness