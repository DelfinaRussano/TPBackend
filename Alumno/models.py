from django.db import models 
 
class Alumno(models.Model): 
    nombre = models.CharField(max_length=100) 
    apellido = models.CharField(max_length=100) 
    DNI = models.IntegerField()
    Ingresos= models.IntegerField()
    MontoDeuda = models.IntegerField()
 
    def __str__(self): 
        return f"{self.nombre} {self.apellido}"