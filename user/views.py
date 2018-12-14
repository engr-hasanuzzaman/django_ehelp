from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.conf.urls import handler403

# Create your views here.
def sign_up(request):
  if request.method == 'POST':
    # user registration
    return handler403(request, None)
  else:
    form = UserCreationForm()
    return render(request, 'user/new.html', {'form': form})
