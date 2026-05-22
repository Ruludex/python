from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    
    # 💡 Dejamos este como 'ver_perfil' para que el inicio.html y perfil.html lo encuentren
    path('perfil/', views.ver_perfil, name='ver_perfil'),  
    
    # 🛠️ ESTA ES LA LÍNEA QUE FALTA AGREGAR:
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
]