from .models import Plan  #enlace con views

def crear_plan_service(datos):
    nombre = datos.get("nombre", "").strip()
    descripcion = datos.get("descripcion", "").strip()
    precio = datos.get("precio", "").strip()
    duracion = datos.get("duracion", "").strip()

    if not nombre or not precio or not duracion:
        return False, "Nombre, precio y duración son obligatorios."

    try:
        precio = float(precio)
    except ValueError:
        return False, "El precio debe ser un número válido."

    Plan.objects.create(
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        duracion=duracion,
    )

    return True, "Plan creado correctamente."
