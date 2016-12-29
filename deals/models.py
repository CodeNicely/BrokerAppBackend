#!/usr/local/bin/python
# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class product_data(models.Model):	
	category_id=models.IntegerField(default=0)
	name=models.CharField(max_length=128,null=False,blank=False)
	description=models.CharField(max_length=255,null=False,blank=False)
	price=models.IntegerField(default=0)
 	UNIT_CHOICES = (
    ('Ton ( टन )', "Ton ( टन )"),
    ('Quintal ( क्विंटल )', "Quintal ( क्विंटल )"))
	unit=models.CharField(choices=UNIT_CHOICES,max_length=20,null=False,default='Quintal ( क्विंटल )')
	image=models.ImageField(upload_to='product/',default="/media/product/default.png")
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)	
	show=models.BooleanField(default=False)

class category_data(models.Model):
	name=models.CharField(max_length=128,blank=False,null=False,default='Not Available')
	description=models.CharField(max_length=255,blank=False,null=False,default='Not Available')
	show=models.BooleanField(default=False)

class unit_data(models.Model):
	UNIT_CHOICES = (
    ('Ton ( टन )', "Ton ( टन )"),
    ('Quintal ( क्विंटल )', "Quintal ( क्विंटल )"))
	name=models.CharField(choices=UNIT_CHOICES,max_length=20,null=False,default='Quintal ( क्विंटल )')
	