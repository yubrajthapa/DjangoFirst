from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class NewUserForm(UserCreationForm):
    username = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    password1 = forms.CharField(required = True)
    password2 = forms.CharField(required = True) 
    

    class meta:
        model = User
        fields = ("Username","email", "password1", "password2")


