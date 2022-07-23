from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.register(Product)
# Displays the 'id', 'name'of the product in admin pannel
class ProductModelAdmin(admin.ModelAdmin):
    list_display=["id", "name", "price"]