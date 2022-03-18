from django.urls import path 
from AppIntegrantes.views import *

urlpatterns = [
    path('familiares/', familiares)
]
