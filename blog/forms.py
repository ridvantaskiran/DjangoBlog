from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Author


# Create your forms here.

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class AuthorForm(forms.ModelForm):
    
    birthday = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))

    class Meta:
        model = Author
        fields = ['birthday']