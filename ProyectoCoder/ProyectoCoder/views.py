from datetime import datetime
from django.template import Template, Context, loader
from django.http import HttpResponse


def root_view(request):
    return HttpResponse("Pagina de inicio por defecto")


""" def primer_vista(request):
    return HttpResponse("Hola salsa!!!")


def primer_vista(request):
    return HttpResponse("<h1>Hola Salsa!</h1>")


def dia_hora(request):
    fecha_hora = datetime.now()
    return HttpResponse(f"<h4>Fecha: {fecha_hora} </h4>")


def nombre_usuario(request, nombre):
    return HttpResponse(f"Tu nombre es {nombre}")


def edad_usuario(request, edad):
    anio_nacimiento = 2022 - int(edad)
    return HttpResponse(f"Usted nació en el {anio_nacimiento}")
 """

""" def pagina_inicio(request):
    archivo = open(r"D:\proyecto coder\djangoProyecto\ProyectoCoder\ProyectoCoder\templates\page.html" , 'r')
    
    nombre = "nacho"
    apellido = "perez"
    fecha_hora = datetime.now()
    
    listado_calificaciones = [10, 8, 5]
    
    #dicionario con los datos que mandaremos como contexto
    dict_context = {"nombre": nombre, "apellido": apellido, "fecha_hora": fecha_hora, "listado": listado_calificaciones}
    
    plantilla = Template(archivo.read())
    
    archivo.close()
    
    context = Context(dict_context)
    
    documento = plantilla.render(context)
    
    return HttpResponse(documento) """


def pagina_inicio(request):

    nombre = "nacho"
    apellido = "perez"
    fecha_hora = datetime.now()

    listado_calificaciones = [10, 8, 5]

    # dicionario con los datos que mandaremos como contexto
    dict_context = {"nombre": nombre, "apellido": apellido,
                    "fecha_hora": fecha_hora, "listado": listado_calificaciones}

    plantilla = loader.get_template("page.html")

    documento = plantilla.render(dict_context)

    return HttpResponse(documento)
