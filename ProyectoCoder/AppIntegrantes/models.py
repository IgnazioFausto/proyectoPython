from pydoc import render_doc
from django.db import models
from django.http import HttpResponse
# Create your models here.


class Integrante(models.Model):

    nombre = models.CharField(max_length=40)
    dni = models.IntegerField(primary_key=True)
    fecha_nacimiento = models.DateField()
    
    doc = f"Nombre {nombre} DNI {dni} Fecha Nacimiento {fecha_nacimiento}"
    
    


