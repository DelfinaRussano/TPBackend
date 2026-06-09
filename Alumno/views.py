from django.shortcuts import render
from Alumno.models import Alumno
from Clase.models import Clase
from Plan.models import Plan
from Profesor.models import Profesor
from Reclamos.models import Reclamos

# Create your views here.

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'listaAlumnos.html', {'alumnos': alumnos})


def admin_panel(request):
    alumnos = Alumno.objects.all()
    clases = Clase.objects.all()
    profesores = Profesor.objects.all()
    planes = Plan.objects.all()
    reclamos = Reclamos.objects.all()

    context = {
        'alumnos': alumnos,
        'clases': clases,
        'profesores': profesores,
        'planes': planes,
        'reclamos': reclamos,
    }

    return render(request, 'admin.html', context)
