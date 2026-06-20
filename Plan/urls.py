from django.urls import path
from . import views

app_name = 'plan'

urlpatterns = [
    path('crear/', views.crear_plan, name='crear_plan'),
]
