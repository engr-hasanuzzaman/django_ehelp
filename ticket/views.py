from django.shortcuts import render
from django.http import HttpResponse
from .models import Ticket
from .forms import TicketForm

# Create your views here.
def ticket_list(request):
  tickets = Ticket.objects.all()
  return render(request, 'ticket/index.html', {'tickets': tickets})

def show(request, pk):
  ticket = Ticket.objects.get(pk=pk)
  return render(request, 'ticket/show.html', {'ticket': ticket})

def new(request):
  if request.method == 'POST':
    form = TicketForm(request.POST)
    if form.is_valid():
      ticket = form.save(commit=False)
  else:
    form = TicketForm()
    return render(request, 'ticket/new.html', {'form': form})
