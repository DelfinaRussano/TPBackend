from django.urls import path
from . import views

app_name = 'profesor'

urlpatterns = [
    path('crear/', views.crear_profesor, name='crear_profesor'),
]
