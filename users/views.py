from django.shortcuts import render, redirect
from . forms import NewUserForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST) #accessing POST data from the NewUserForm and saving it to form
        if form.is_valid(): # checks if the form data is valid
            user = form.save() # if the form is valid it calls the save method from the forms.py
            return redirect('/myapp/products')
    form = NewUserForm()
    context = {
        'form':form,
    }
    return render(request, 'users/register.html',context)

 
