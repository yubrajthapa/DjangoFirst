from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.site_header = "Buy & Sell Website"
admin.site.site_title = "Buy Best"
admin.site.index_title = "Manage Buying Website"

# Displays the 'id', 'name'of the product in admin pannel
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'desc','id')
    search_fields = ('name',)


admin.site.register(Product,ProductAdmin)

