from __future__ import unicode_literals

from django.db import models

# Create your models here.
class order_data(models.Model):
    order_id=models.CharField(max_length=20,blank=True,null=True)
    buyer_id=models.CharField(max_length=20,blank=True,null=True)
    seller_id=models.CharField(max_length=20,blank=True,null=True)
    product_id=models.IntegerField(default=0)
    product_name=models.CharField(max_length=56,blank=True,null=True)
    product_quantity=models.DecimalField(max_digits=10,decimal_places=2)
    buying_price=models.IntegerField(default=0)
    selling_price=models.IntegerField(default=0)
    truck_number=models.CharField(max_length=32,blank=True,null=True)
    description=models.CharField(max_length=512,blank=True,null=True)
    show=models.BooleanField(default=True)
    modified= models.DateTimeField(auto_now=True,auto_now_add=False)
    created= models.DateTimeField(auto_now=False,auto_now_add=True)