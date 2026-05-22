from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comentario  # 👈 Sumamos 'Comentario'
from .forms import ComentarioForm      # 👈 Sumamos el formulario de comentarios

def inicio(request):
    # 1. Si un usuario envía un comentario (petición POST)
    if request.method == 'POST':
        # Validamos que el usuario esté logueado (hijo registrado) para poder comentar
        if request.user.is_authenticated:
            form = ComentarioForm(request.POST)
            post_id = request.POST.get('post_id') # Detectamos a qué post pertenece el comentario
            post_actual = Post.objects.get(id=post_id)
            
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.post = post_actual   # Vinculamos el comentario a ese post "padre"
                comentario.autor = request.user  # Guardamos automáticamente al usuario logueado como autor
                comentario.save()               # Se guarda de forma independiente en la base de datos
                return redirect('inicio')       # Recargamos la página para ver el comentario al toque
            
    # 2. Si solo entran a mirar la página (petición GET normal)
    posts = Post.objects.all().order_by('-fecha_publicacion')
    form = ComentarioForm() # Pasamos el formulario vacío para que se renderice en el HTML
    
    return render(request, 'inicio.html', {'posts': posts, 'form': form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/registro.html', {'form': form})