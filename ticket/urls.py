from django.urls import path
from . import views

urlpatterns = [
  path('', views.ticket_list, name='ticket_index'),
  path('ticket/<int:pk>', views.show, name='show_ticket')
]