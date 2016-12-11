from django.contrib import admin
from .models import *
# Register your models here.

class otp_infoAdmin(admin.ModelAdmin):
	list_display=["mobile","modified"]

admin.site.register(otp_info,otp_infoAdmin)


