from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Plan


def crear_plan(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        descripcion = request.POST.get('descripcion', '').strip()
        precio = request.POST.get('precio', '').strip()
        duracion = request.POST.get('duracion', '').strip()

        if not nombre or not precio or not duracion:
            messages.error(request, 'Nombre, precio y duración son obligatorios.')
            return render(request, 'crear_plan.html', {
                'nombre': nombre,
                'descripcion': descripcion,
                'precio': precio,
                'duracion': duracion,
            })

        try:
            precio_decimal = float(precio)
        except ValueError:
            messages.error(request, 'El precio debe ser un número válido.')
            return render(request, 'crear_plan.html', {
                'nombre': nombre,
                'descripcion': descripcion,
                'precio': precio,
                'duracion': duracion,
            })

        Plan.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio_decimal,
            duracion=duracion,
        )
        messages.success(request, 'Plan creado correctamente.')
        return redirect('admin_panel')

    return render(request, 'crear_plan.html')
