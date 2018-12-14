from . import views
from django.urls import path, re_path

urlpatterns = [
  path('new/', views.sign_up, name='signup'),
  path('login/', views.sign_in, name='signin')
]