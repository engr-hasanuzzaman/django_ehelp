from django.urls import path, re_path
from . import views

urlpatterns = [
  path('', views.ticket_list, name='ticket_index'),
  path('ticket/<int:pk>', views.show, name='show_ticket'),
  path('tickets/new/', views.new, name='new_ticket')
]