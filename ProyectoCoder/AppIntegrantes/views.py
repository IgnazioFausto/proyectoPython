from AppIntegrantes.models import Integrante
from django.http import HttpResponse

# Create your views here.

def familiares(request):
    
    integrante = Integrante(nombre='Juan', dni=12345678, fecha_nacimiento='1995-01-05')
    
    integrante.save()
    
    doc = f"Nombre {integrante.nombre} DNI {integrante.dni} Fecha Nacimiento {integrante.fecha_nacimiento}"

    return HttpResponse(doc)

