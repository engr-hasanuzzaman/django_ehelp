from . import views
from django.urls import path, re_path

urlpatterns = [
  path('new/', views.sign_up, name='new_user')
]