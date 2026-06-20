from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profesor
from Clase.models import Clase


def crear_profesor(request):
	if request.method == 'POST':
		nombre = request.POST.get('nombre', '').strip()
		apellido = request.POST.get('apellido', '').strip()
		clases_ids = request.POST.getlist('clases')

		if not nombre or not apellido:
			messages.error(request, 'Nombre y apellido son obligatorios.')
			clases = Clase.objects.all()
			return render(request, 'crear_profesor.html', {'clases': clases, 'nombre': nombre, 'apellido': apellido})

		profesor = Profesor.objects.create(nombre=nombre, apellido=apellido)
		if clases_ids:
			profesor.clases.set(clases_ids)
		messages.success(request, 'Profesor creado correctamente.')
		return redirect('admin_panel')

	clases = Clase.objects.all()
	return render(request, 'crear_profesor.html', {'clases': clases})
