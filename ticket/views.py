from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ticket_list(request):
  return HttpResponse("Welcome to you custom url")