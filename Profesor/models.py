from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    clases = models.ManyToManyField('Clase.Clase', related_name='profesores')
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"