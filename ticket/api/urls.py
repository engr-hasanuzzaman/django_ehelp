from django.urls import path
from ticket.api import views

urlpatterns = [
    path('tickets/', views.ListTicket.as_view()),
    path('tickets/<int:pk>/', views.DetailTicket.as_view()),
]