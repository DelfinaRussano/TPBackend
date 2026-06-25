import unicodedata

from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Profesor
from Clase.models import Clase
from django.contrib.auth.decorators import login_required
from accounts.decorators import profesor_required

User = get_user_model()


def normalize_name(value):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', value)
        if c.isalnum() or c == '.'
    ).strip('.').lower()


def generate_unique_email(nombre, apellido):
    base = f"{normalize_name(nombre)}.{normalize_name(apellido)}"
    email = f"{base}@centergym.com"
    suffix = 0
    while User.objects.filter(email=email).exists():
        suffix += 1
        email = f"{base}{suffix}@centergym.com"
    return email


# Muestra las clases asignadas a un profesor específico
@login_required(login_url='home')
@profesor_required
def mis_clases(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    clases = profesor.clases.all()
    q = request.GET.get('q')
    if q:
        clases = clases.filter(nombre__icontains=q)
    return render(request, 'mis_clases_profesor.html', {
        'profesor': profesor,
        'clases': clases,
    })

# Muestra los alumnos de una clase específica de un profesor
@login_required(login_url='home')
@profesor_required
def alumnos_por_clase(request, profesor_id, clase_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    clase = get_object_or_404(Clase, id=clase_id)
    alumnos = clase.alumnos.all()
    q = request.GET.get('q')
    if q:
        alumnos = alumnos.filter(nombre__icontains=q)
    return render(request, 'alumnos_por_clase.html', {
        'profesor': profesor,
        'clase': clase,
        'alumnos': alumnos,
    })

# Muestra el listado completo de profesores
@login_required(login_url='home')
@profesor_required
def lista_profesores(request):
    profesores = Profesor.objects.all()
    q = request.GET.get('q')
    if q:
        # Filtra los profesores cuyo nombre o apellido contenga ese texto
        profesores = profesores.filter(
            Q(nombre__icontains=q) | Q(apellido__icontains=q)
        )
    # Renderiza el template enviando la lista de profesores
    return render(request, 'lista_profesores.html', {
        'profesores': profesores,
    })


def crear_profesor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        apellido = request.POST.get('apellido', '').strip()
        clases_ids = request.POST.getlist('clases')

        if not nombre or not apellido:
            messages.error(request, 'Nombre y apellido son obligatorios.')
            clases = Clase.objects.all()
            return render(request, 'crear_profesor.html', {'clases': clases, 'nombre': nombre, 'apellido': apellido})

        email = generate_unique_email(nombre, apellido)
        try:
            with transaction.atomic():
                profesor = Profesor.objects.create(nombre=nombre, apellido=apellido)
                if clases_ids:
                    profesor.clases.set(clases_ids)

                usuario = User.objects.create_user(
                    email=email,
                    password='profesor',
                    role=User.PROFESOR,
                    first_name=nombre,
                    last_name=apellido,
                )
                usuario.profesor = profesor
                usuario.save()

            messages.success(request, f'Profesor creado correctamente. Email: {email} / Contraseña inicial: profesor')
            return redirect('admin_panel')
        except Exception:
            messages.error(request, 'Error al crear el profesor. Por favor revise los datos e intente nuevamente.')
            clases = Clase.objects.all()
            return render(request, 'crear_profesor.html', {'clases': clases, 'nombre': nombre, 'apellido': apellido})

    clases = Clase.objects.all()
    return render(request, 'crear_profesor.html', {'clases': clases})

