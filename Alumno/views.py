from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from Alumno.models import Alumno
from Clase.models import Clase
from Plan.models import Plan
from Profesor.models import Profesor
from Reclamos.models import Reclamos

# ==========================================
# VISTAS EXISTENTES
# ==========================================

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'listaAlumnos.html', {'alumnos': alumnos})

<<<<<<< HEAD

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
=======
# ==========================================
# NUEVAS VISTAS PARA EL MÓDULO ALUMNO
# ==========================================

def mis_clases(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)
    clases = alumno.clases.all()

    q = request.GET.get('q')
    if q:
        clases = clases.filter(nombre__icontains=q)

    return render(request, 'mis_clases.html',{
        'alumno': alumno,  
        'clases': clases,
    })

def mis_reclamos(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)
    reclamos = alumno.reclamos.all().order_by('-fecha_reclamo')

    return render(request, 'mis_reclamos.html', {
       'alumno': alumno,
       'reclamos': reclamos, 
    })

def crear_reclamo(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)

    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        if contenido:
            Reclamos.objects.create(
                alumno=alumno,
                contenido=contenido,
                estado='Pendiente'
            )
            messages.success(request, 'Reclamo enviado correctamente.')
            return redirect('alumno:mis_reclamos', alumno_id=alumno.id)
        else:
            messages.error(request, 'el contenido del reclamo no puede estar vacio.')

    return render(request, 'crear_reclamo.html', {'alumno': alumno})
>>>>>>> origin/main
