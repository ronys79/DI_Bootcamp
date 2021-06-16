from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
# populate slug to rule out errors + populated field all lower case with hyphen as space
    prepopulated_fields = {'slug': ('product_name',)}
# what to display on admin panel for ref
    list_display = ('category', 'product_name', 'price', 'images', 'stock', 'is_available', 'modified_date')
# clickable links to get to product specific page or quck view image
    list_display_links = ('category', 'product_name', 'images')
    
admin.site.register(Product, ProductAdmin)