from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_url', 'stock', 'created_at')

admin.site.register(Product, ProductAdmin)
