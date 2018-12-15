from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
  username = forms.CharField(label='test', widget=forms.TextInput(attrs={'class': 'form-control'}))
  password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))