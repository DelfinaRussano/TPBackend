from django.db import models

# Create your models here.
class Reclamos(models.Model):
    alumno = models.ForeignKey('Alumno.Alumno', on_delete=models.CASCADE, related_name='reclamos')
    contenido = models.TextField()
    estado = models.CharField(max_length=20, default='Pendiente')
    fecha_reclamo = models.DateTimeField(auto_now_add=True)
    fecha_resolucion = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Reclamo de {self.alumno} - {self.estado}"
