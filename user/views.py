from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.
def sign_up(request):
  if request.method == 'POST':
    # user registration
    return None
  else:
    form = UserCreationForm()
    return render(request, 'user/new.html', {'form': form})
