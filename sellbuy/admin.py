from django.contrib import admin
from .models import *
# Register your models here.

class sell_buy_dataAdmin(admin.ModelAdmin):
	list_display=["id","category_id","mobile","product_name","product_description","product_price","product_unit","created","modified"]
admin.site.register(sell_buy_data,sell_buy_dataAdmin)