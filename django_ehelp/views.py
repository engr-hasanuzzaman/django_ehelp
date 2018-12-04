from django.http import HttpResponse

def index(request):
  return HttpResponse("Hellow world Django")

def hello(request):
  return HttpResponse('Well come to Django learning')
