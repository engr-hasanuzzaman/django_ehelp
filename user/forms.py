from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
  username = forms.CharField(label='test')
  password = forms.CharField(label='password', widget=forms.PasswordInput())