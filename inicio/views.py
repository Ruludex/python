from django.shortcuts import render
from .models import Post  # 👈 Importamos tus Posts para poder usarlos

def inicio(request):
    # 1. Traemos todos los posts ordenados por fecha (el más nuevo primero)
    posts = Post.objects.all().order_by('-fecha_publicacion')
    
    # 2. Le pasamos esos posts al HTML metiéndolos en el diccionario
    return render(request, 'inicio.html', {'posts': posts})