from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Post

def inicio(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')
    return render(request, 'inicio.html', {'posts': posts}) # 👈 Este está suelto, así que queda igual

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    # 👇 CAMBIÁ ESTA LÍNEA (Pusimos 'registration/' en lugar de 'inicio/')
    return render(request, 'registration/registro.html', {'form': form})