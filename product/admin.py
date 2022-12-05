from django.contrib import admin
from product.models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name','price')
    list_display = ('name','price','minimum','amount_per_package','max_availability')
    list_display_links = ('name','price','minimum','amount_per_package','max_availability')

admin.site.register(Product, ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ('product_id','quantity','price','subtotal')

admin.site.register(Cart, CartAdmin)