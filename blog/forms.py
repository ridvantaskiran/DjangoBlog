from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Author


# Create your forms here.

class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class AuthorForm(forms.ModelForm):
    
    birthday = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))

    class Meta:
        model = Author
        fields = ['birthday']