from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):

    return render(request, "AppIntegrantes/inicio.html" )

def estudiantes(request):

    return render(request, "AppIntegrantes/estudiantes.html" )

def profesores(request):

    return render(request, "AppIntegrantes/profesores.html" )