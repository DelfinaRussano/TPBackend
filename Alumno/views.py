from django.shortcuts import render
from .models import Alumno

# Create your views here.

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'listaAlumnos.html', {'alumnos': alumnos})
