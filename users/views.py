from django.shortcuts import render, redirect
from . forms import NewUserForm
from django.contrib.auth.decorators import login_required

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

#This will check if the user is logged in before running this views. 
# If the user is not logged in this view will not be running
@login_required 
def profile(request):
    return render(request, 'users/profile.html')