from django.urls import path 
from AppIntegrantes.views import *

urlpatterns = [
    path('' , inicio, name='inicio'),
    path('estudiantes' , estudiantes, name='estudiantes'),
    path('profesores' , profesores, name='profesores'),
]
