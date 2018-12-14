from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.conf.urls import handler403
from .forms import UserLoginForm

# Create your views here.
def sign_up(request):
  print('---with in sing_up method')
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
  print('---with in sign_in method')
  if request.method == 'POST':
    form = UserLoginForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password')
      user = authenticate(username = username, password = raw_password)
      print("user is %s"%(user))
      if user:
          login(request, user)
      return redirect('home')
      
  else:    
    form = UserLoginForm()

  return render(request, 'user/signin.html', {'form': form})

def signout(request):
  if request.user.is_authenticated:
    logout(request)
    return redirect('home')
  else:  
    return redirect('home')