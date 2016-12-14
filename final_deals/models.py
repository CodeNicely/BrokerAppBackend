from __future__ import unicode_literals

from django.db import models

# Create your models here.


class deals(models.Model):
	
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	#mobile=models.IntegerField(default=0)
	quantity=models.IntegerField(blank=False)
	product_name=models.CharField(max_length=120,null=False,blank=False)
	quality=models.CharField(max_length=120,default=0)
	price=models.IntegerField(default=0)
	#catigory=models.CharField(max_length=10,default="seller",blank=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
