from django.db import models
from django.contrib.auth.models import User # Importamos el modelo de usuarios nativo de Django

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    # 💡 CORREGIDO: Ahora cada Post tiene un autor vinculado a la base de datos
    # Usamos null=True y blank=True por si tenés posts viejos creados sin autor, así no se te rompe la BD.
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)

    def __str__(self):
        # Mostramos también el autor en el panel de administración para que sea más claro
        return f"'{self.titulo}' por {self.autor.username if self.autor else 'Anónimo'}"


class Comentario(models.Model):
    # Relaciona el comentario con tu modelo Post. 
    # Si borrás un Post, se borran automáticamente sus comentarios (on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    
    # Guarda automáticamente qué usuario (de los que se registran en tu blog) escribió el comentario
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.username} en '{self.post.titulo}'"


class Perfil(models.Model):
    # Relación 1 a 1: un usuario tiene un perfil, un perfil pertenece a un usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    
    # Campo para la foto: se van a guardar en la carpeta 'media/perfiles/'
    # Si el usuario no sube foto, usamos una por defecto (default.png)
    foto = models.ImageField(default='perfiles/default.png', upload_to='perfiles/')
    
    # Campo para la biografía (opcional, máximo 300 caracteres)
    biografia = models.TextField(max_length=300, blank=True)
    
    # Fecha de creación automática
    fecha_union = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"


# ⚡ TRUCO MÁGICO: Crear el perfil automáticamente al registrarse
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)