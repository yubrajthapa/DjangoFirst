from django.contrib import admin
from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    #path('products/', views.products, name='products'), #url for function based view
    path('products/', views.ProductListView.as_view(), name='products'), #url for class based view 
    #path('products/<int:id>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    #path('products/add/', views.add_product, name='add_product'),
    path('products/add/', views.ProuctCreateView.as_view(), name='add_product'),
    #path('products/update/<int:id>/', views.update_product, name='update_product'),
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    #path('products/delete/<int:id>/', views.delete_product, name='delete_product'),
    path('products/delete/<int:pk>/', views.ProductDelete.as_view(), name='delete_product'),
    path('products/mylistings/', views.my_listings, name='mylistings'),
]
 



 