from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    path_img = models.CharField(max_length=255 , default = '')
    url_img = models.CharField(max_length=255 , default = '')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField( default = True )
    created_at = models.DateTimeField(auto_now_add=True)