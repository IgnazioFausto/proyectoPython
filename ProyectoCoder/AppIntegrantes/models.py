from django.db import models

# Create your models here.


class Integrante(models.Model):

    nombre = models.CharField(max_length=40)
    dni = models.IntegerField(primary_key=True)
    fecha_nacimiento = models.DateField()


