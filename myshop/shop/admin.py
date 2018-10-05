# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-01T15:27:13-07:00
# @Email:  agupta@juniper.net
# @Filename: admin.py
# @Last modified by:   agupta
# @Last modified time: 2018-10-01T15:37:40-07:00

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)
