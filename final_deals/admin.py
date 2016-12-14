from django.contrib import admin
from .models import *
# Register your models here.

class dealsAdmin(admin.ModelAdmin):

	list_display=["product_name","quality","quantity","price","modified"]


admin.site.register(deals,dealsAdmin)
