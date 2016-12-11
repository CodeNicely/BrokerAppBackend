from __future__ import unicode_literals

from django.db import models

# Create your models here.

class login_user(models.Model):
	name= models.CharField(max_length=120,null=False,blank=False)
	firm_name= models.CharField(max_length=240,null=False,blank=False)
	city= models.CharField(max_length=240,null=False,blank=False)
	mobile=models.PositiveSmallIntegerField(default=0)
	catigory=models.CharField(max_length=120,null=False,blank=False,default="buyer")
