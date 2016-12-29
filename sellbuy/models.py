#!/usr/local/bin/python
# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class sell_buy_data(models.Model):	
	category_id=models.IntegerField(default=0)
	mobile=models.PositiveSmallIntegerField(default=0)
	product_name=models.CharField(max_length=128,null=False,blank=False)
	product_description=models.CharField(max_length=255,null=False,blank=False)
	product_price=models.IntegerField(default=0)
 	UNIT_CHOICES = (
    ('Ton ( टन )', "Ton ( टन )"),
    ('Quintal ( क्विंटल )', "Quintal ( क्विंटल )"))
	product_unit=models.CharField(choices=UNIT_CHOICES,max_length=20,null=False,default='Quintal ( क्विंटल )')
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)	
	