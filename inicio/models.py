from django.db import models
from django.contrib.auth.models import User # 👈 Importamos el modelo de usuarios nativo de Django

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# 🔽 AGREGAMOS ESTO ABAJO DE TU POST 🔽

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