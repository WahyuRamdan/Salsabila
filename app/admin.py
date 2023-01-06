from django.contrib import admin
from .models import * 

class MapsAdmin(admin.ModelAdmin):
    list_display = ['kota']

class TableAdmin(admin.ModelAdmin):
    list_display = ['provinsi']


admin.site.register(Maps, MapsAdmin)
admin.site.register(Table, TableAdmin)