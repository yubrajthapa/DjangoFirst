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

    #Custom Action methods
    def set_price_to_zero(self,request,queryset):
        queryset.update(price = 0)
    actions = ('set_price_to_zero',) #displays this option in action
    #queryset are those products selected by user on which we want to perform this aciton

admin.site.register(Product,ProductAdmin)

