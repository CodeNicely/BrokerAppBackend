from django.contrib import admin
from .models import version_data
# Register your models here.

class version_dataAdmin(admin.ModelAdmin):
	list_display=["version","compulsory_update"]

admin.site.register(version_data,version_dataAdmin)

