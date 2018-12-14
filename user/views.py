from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.conf.urls import handler403
from .forms import UserLogin

# Create your views here.
def sign_up(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('home')
  else:
    form = UserCreationForm()
  return render(request, 'user/new.html', {'form': form})

def sign_in(request):
  if request.method == 'POST':
    form = UserLogin(request.POST)
    if form.is_valid():
      u_name = authenticate(username=form.cleaned_data.get('username'))
      u_pass = authenticate(username=form.cleaned_data.get('password'))
      user = authenticate(username = u_name, password = u_pass)
      login(request, user)
      return redirect('home')
  else:    
    form = UserLogin()
    
  return render(request, 'user/signin.html', {'form': form})