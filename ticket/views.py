from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ticket
from django.contrib.auth.models import User
from .forms import TicketForm
from django.conf.urls import handler403

# Create your views here.
def ticket_list(request):
  tickets = Ticket.objects.filter(creator=request.user)
  return render(request, 'ticket/index.html', {'tickets': tickets})

def show(request, pk):
  ticket = Ticket.objects.get(pk=pk)
  return render(request, 'ticket/show.html', {'ticket': ticket})

def new(request):
  if not request.user.is_authenticated:
    return redirect('home')

  if request.method == 'POST':
    form = TicketForm(request.POST)
    if form.is_valid():
      ticket = form.save(commit=False)
      ticket.creator = request.user
      ticket.save()
      return redirect('show_ticket', pk=ticket.pk)
  else:
    form = TicketForm()
    return render(request, 'ticket/new.html', {'form': form})
