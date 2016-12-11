from django.contrib import admin
from .models import *
# Register your models here.

class keys_Admin(admin.ModelAdmin):
	list_display=["key","value","created","modified"]

admin.site.register(keys,keys_Admin)
	
	

