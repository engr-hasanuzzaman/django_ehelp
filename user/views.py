from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from rest_framework.response import Response
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
      return redirect('ticket_index')
      
  else:    
    form = UserLoginForm()

  return render(request, 'user/signin.html', {'form': form})

def signout(request):
  if request.user.is_authenticated:
    logout(request)
    return redirect('home')
  else:  
    return redirect('home')




@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)    