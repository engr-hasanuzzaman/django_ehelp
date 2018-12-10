from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
  class Meta:
    model = Ticket
    fields = ('title', 'description', 'status')
    widgets = {
          'title': forms.TextInput(attrs={'class': 'form-control'}),
          'description': forms.Textarea(attrs={'class': 'form-control'}),
          'status': forms.TextInput(attrs={'class': 'form-control'})
        }
