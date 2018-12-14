from django import forms
from django.contrib.auth.models import User

class UserLogin():
  username = forms.TextInput(attrs={'class': 'form-control'})
  password = forms.PasswordInput(attrs={'class': 'form-control'})
