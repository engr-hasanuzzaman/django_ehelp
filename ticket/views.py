from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ticket_list(request):
  return render(request, 'ticket/index.html', {})