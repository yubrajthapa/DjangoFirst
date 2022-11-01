from audioop import reverse
from curses.ascii import HT
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


# Accessing and displaying data from database.
def products(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'myapp/index.html', context)


# Class based views for above products view[ListView]
class ProductListView(ListView):
    model = Product
    template_name= 'myapp/index.html'
    context_object_name = 'products'
    paginate_by = 4
    


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product' : product
    }
    return render(request, 'myapp/detail.html', context)

# Class based view for above product detail view[DetailView]
class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/detail.html'
    context_object_name = 'product'

@login_required
def add_product(request):
    if request.method=='POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        seller_name = request.user #Sets currently loggedin user as seller name
        # Saving these data into the database
        product = Product(name=name,price=price, desc=desc,image=image,seller_name=seller_name)
        product.save()
    return render(request, 'myapp/addproduct.html')

# Class based view for creating  a product
class ProuctCreateView(CreateView):
    model = Product
    fields = ['name','price','desc','image','seller_name']


def update_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        product.image = request.FILES['upload']
        product.save()
        return redirect('/myapp/products')
    context = {
        'product' : product
    }
    return render(request,'myapp/updateproduct.html',context)

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name','price','desc','image','seller_name']
    template_name_suffix = '_update_form'

def delete_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        product.delete()
        return redirect('/myapp/products')
    context = {
        'product': product,
    }
    return render(request,'myapp/delete.html',context)


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('myapp:products')
   

   
def my_listings(request):
    products = Product.objects.filter(seller_name=request.user)
    context = {
        'products': products
    }
    return render(request, 'myapp/mylistings.html', context)