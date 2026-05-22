from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'), # 👈 Asegurate de que esta coma esté acá
    path('registro/', views.registro, name='registro'), # 👈 Y esta también
]