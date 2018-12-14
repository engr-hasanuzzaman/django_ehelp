from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  return render(request, 'home.html')

def hello(request):
  return HttpResponse('Well come to Django learning')
