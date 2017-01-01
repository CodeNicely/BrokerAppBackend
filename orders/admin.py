from django.contrib import admin
from .models import *

# Register your models here.
class order_dataAdmin(admin.ModelAdmin):
	list_display=["order_id","buyer_id","seller_id","product_id","product_name","product_quantity","buying_price","selling_price","truck_number","show","modified","created"]
admin.site.register(order_data,order_dataAdmin)



