from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Clase


def crear_clase(request):
	if request.method == 'POST':
		nombre = request.POST.get('nombre', '').strip()
		dias = request.POST.get('dias', '').strip()
		horario = request.POST.get('horario', '').strip()

		if not nombre:
			messages.error(request, 'El nombre de la clase es obligatorio.')
			return render(request, 'crear_clase.html', {'nombre': nombre, 'dias': dias, 'horario': horario})

		Clase.objects.create(nombre=nombre, dias=dias, horario=horario)
		messages.success(request, 'Clase creada correctamente.')
		return redirect('admin_panel')

	return render(request, 'crear_clase.html')
