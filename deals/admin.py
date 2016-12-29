from django.contrib import admin
from .models import *

# Register your models here.
class category_dataAdmin(admin.ModelAdmin):
	list_display=["id","name","description"]
admin.site.register(category_data,category_dataAdmin)

class product_dataAdmin(admin.ModelAdmin):
	list_display=["id","name","category_id","description","image","price","unit","created","modified","show"]
admin.site.register(product_data,product_dataAdmin)

class unit_dataAdmin(admin.ModelAdmin):
	list_display=["id","name"]
admin.site.register(unit_data,unit_dataAdmin)