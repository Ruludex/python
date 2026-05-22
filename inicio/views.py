from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required # Para proteger el perfil
from .models import Post, Comentario, Perfil  # Asegurate de importar tu modelo Perfil aquí
from .forms import ComentarioForm, PerfilForm  # Sumamos PerfilForm aquí

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

# ==========================================
# VISTAS PARA EL PERFIL DE USUARIO
# ==========================================

@login_required # Si no está logueado, Django lo rebota al login automáticamente
def ver_perfil(request):
    try:
        # Intentamos obtener el perfil del usuario actual
        perfil = request.user.perfil
    except Perfil.DoesNotExist:
        # Si el usuario no lo tiene creado en la BD, se lo creamos en el acto
        perfil = Perfil.objects.create(user=request.user)
        
    # Pasamos el perfil seguro a la plantilla
    return render(request, 'perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    try:
        # Validamos también acá que el perfil exista antes de intentar editarlo
        perfil = request.user.perfil
    except Perfil.DoesNotExist:
        perfil = Perfil.objects.create(user=request.user)
    
    if request.method == 'POST':
        # request.FILES es obligatorio acá para recibir la imagen de la foto
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            # 💡 CORREGIDO: Redireccionamos a 'ver_perfil' que es el nombre real en tu urls.py
            return redirect('ver_perfil') 
    else:
        # Si entra de forma normal, carga el formulario con los datos que ya tenía guardados
        form = PerfilForm(instance=perfil)
        
    return render(request, 'editar_perfil.html', {'form': form})