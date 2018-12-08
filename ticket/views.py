from django.shortcuts import render
from django.http import HttpResponse
from .models import Ticket

# Create your views here.
def ticket_list(request):
  tickets = Ticket.objects.all()
  return render(request, 'ticket/index.html', {'tickets': tickets})

def show(request, pk):
  ticket = Ticket.objects.get(pk=pk)
  return render(request, 'ticket/show.html', {'ticket': ticket})
