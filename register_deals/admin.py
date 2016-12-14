from django.contrib import admin
from .models import *
# Register your models here.

class offersAdmin(admin.ModelAdmin):
	
	list_display=["mobile","product_name","price","quantity","catigory","is_sent"]

admin.site.register(offers,offersAdmin)
