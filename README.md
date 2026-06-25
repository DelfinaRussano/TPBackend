# 🏋️ Center GYM

Sistema CRM para la gestión integral de gimnasios desarrollado como Trabajo Práctico Final de Backend.

## 📋 Descripción

Center GYM es una aplicación web diseñada para centralizar la gestión administrativa de un gimnasio, permitiendo administrar clientes, profesores, clases, planes y reclamos desde una única plataforma.

El sistema busca reemplazar procesos manuales realizados mediante planillas, papel o aplicaciones de mensajería, mejorando la organización interna y la trazabilidad de la información.

---

## 🎯 Objetivos

- Gestionar clientes del gimnasio.
- Administrar profesores y clases.
- Gestionar planes.
- Administrar reclamos y su seguimiento.
- Centralizar toda la información en una única aplicación.

---

## 👥 Roles del sistema

### Administrador

- Gestión completa del sistema.
- Alta y modificación de clientes.
- Alta y modificación de profesores.
- Gestión de clases.
- Gestión de planes.
- Gestión de reclamos.

### Profesor

- Consulta de clases asignadas.
- Consulta de horarios.

### Alumno

- Consulta de plan activo.
- Consulta de deuda.
- Consulta de clases asignadas.
- Asociarse a clases nuevas.

---

## 🚀 Funcionalidades implementadas

### Clientes

- Alta de clientes.
- Modificación de clientes.
- Consulta de detalle.
- Asociación automática de cuenta de usuario.

### Profesores

- Alta de profesores.
- Asociación a una o varias clases.
- Generación automática de cuenta de usuario.

### Clases

- Alta de clases.
- Asociación de alumnos.
- Asociación de profesores.
- Gestión de horarios.

### Planes

- Creación de planes.

### Reclamos

- Creación de reclamos.
- Seguimiento de estado.
- Visualización de historial.

### Autenticación

- Login mediante email y contraseña.
- Control de acceso por roles:
  - ADMIN
  - PROFESOR
  - ALUMNO

---

## 🛠 Tecnologías utilizadas

### Backend

- Python 3
- Django

### Frontend

- HTML5
- CSS3
- JavaScript

### Base de datos

- SQLlite

### Herramientas

- Git
- GitHub
- Visual Studio Code

---

## 📂 Estructura general

```text
project/
│
├── accounts/
├── alumnos/
├── profesores/
├── clases/
├── planes/
├── reclamos/
│
├── templates/
├── static/
│
├── manage.py
└── requirements.txt
```

---

## ⚙️ Instalación

### 1. Crear entorno virtual

#### Windows

```bash
python -m venv env
```

### 2. Activar entorno virtual

#### CMD

```bash
env\Scripts\activate
```

#### Git Bash

```bash
source env/Scripts/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario admin
Ejecutar el siguiente comando desde la raíz del proyecto:
```bash
python manage.py shell -c "from django.contrib.auth import get_user_model; User=get_user_model(); user, created = User.objects.get_or_create(email='admin@centergym.com', defaults={'role':'ADMIN','is_staff':True,'is_superuser':True,'first_name':'Admin','last_name':'Gym'}); user.set_password('Password123!'); user.is_staff=True; user.is_superuser=True; user.save(); print('Usuario administrador creado')"
```
### 7. Ejecutar servidor

```bash
python manage.py runserver
```

Acceder desde:

```text
http://127.0.0.1:8000
```

---

## 🔐 Usuarios

El sistema permite la generación automática de usuarios para:

### Alumnos

Formato:

```text
nombre.apellido@centergym.com
```

Contraseña inicial:

```text
alumno
```

Rol:

```text
ALUMNO
```

### Profesores

Formato:

```text
nombre.apellido@centergym.com
```

Contraseña inicial:

```text
profesor
```

Rol:

```text
PROFESOR
```

---

## 🗄 Modelo de datos principal

### Entidades principales

- Account
- Alumno
- Profesor
- Clase
- Plan
- Reclamo

### Relaciones

- Un Alumno posee una cuenta.
- Un Profesor posee una cuenta.
- Un Profesor puede dictar múltiples clases.
- Una Clase puede tener múltiples alumnos.
- Un Alumno puede tener un Plan.
- Un Alumno puede generar Reclamos.
- El Administravo puede cambiar el estado del Reclamo.

---

## 📌 Estado actual

Proyecto académico en desarrollo para la materia Backend.

Actualmente se encuentra implementada la estructura principal del CRM, incluyendo:

- Autenticación por roles.
- Gestión de clientes.
- Gestión de profesores.
- Gestión de clases.
- Gestión de planes.
- Gestión de reclamos.
- Asociación automática de cuentas para alumnos y profesores.

---

## 👨‍💻 Integrantes

- Daniela Tassara
- María Florencia Quintana

---

## 📚 Materia

Backend – Trabajo Práctico Final  
IFTS N.º 18

---

## 🔗 Link de documento 
https://docs.google.com/document/d/1cKRof5L0gjuMEg_XriVTVmrj8rJP_-pzNh2WevZqIHA/edit?tab=t.0 

## 🔗 Manual de Usuario Administrador 
https://docs.google.com/document/d/1SAW1Ef2LVLBZyBADx8EzBdzwceo8DFhTZXYC4OMXh1c/edit?usp=sharing 
