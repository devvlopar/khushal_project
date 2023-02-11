from django.db import models

# Create your models here.
class Seller(models.Model):
    full_name = models.CharField(max_length=100)
    gst_no = models.CharField(max_length = 15)
    address = models.TextField(max_length =255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    pic = models.FileField(upload_to= 'profile_pics', default='sad.jpg')

    def __str__(self):
        return self.email