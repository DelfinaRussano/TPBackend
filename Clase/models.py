from django.db import models

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    dias = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    alumnos = models.ManyToManyField('Alumno.Alumno', related_name='clases')

    def __str__(self):
        return self.nombre