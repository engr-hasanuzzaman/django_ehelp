from rest_framework import generics
import ticket.models as models
import ticket.api.serializers as serializers

class ListTicket(generics.ListCreateAPIView):
    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketSerializer


class DetailTicket(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketSerializer