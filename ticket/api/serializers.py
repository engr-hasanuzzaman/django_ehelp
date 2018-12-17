from rest_framework import serializers
from ticket.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'title', 'description', 'status')
    model = Ticket
    