from django.urls import path
from homeapp.views import show_home

app_name = 'homeapp'

urlpatterns = [
    path('', show_home, name='homepage'),
]