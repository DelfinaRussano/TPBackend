from django.urls import path
from . import views

app_name = 'clase'

urlpatterns = [
    path('crear/', views.crear_clase, name='crear_clase'),
]
