from . import views
from django.urls import path, re_path

urlpatterns = [
  path('signup/', views.sign_up, name='signup'),
  path('login/', views.sign_in, name='signin'),
  path('logout/', views.signout, name='logout')
]