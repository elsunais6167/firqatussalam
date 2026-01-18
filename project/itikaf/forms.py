from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=70)
    last_name = forms.CharField(max_length=70)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class Admins(ModelForm):

    mosque = forms.ModelChoiceField(queryset=Mosque.objects.all(), widget=forms.Select(attrs={'class': 'hide-field'}))
    class Meta:
        model = MosqueAdmin
        fields = ['user', 'mosque']
