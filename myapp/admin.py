from django.contrib import admin
from .models import  Cars

# Register your models here.
@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('name', 'about', 'model', 'price','car_type', 'created_at')
    search_fields = ('title',)
