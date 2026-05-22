from django.contrib import admin
from .models import Post, Comentario # 👈 Asegurate de importar Comentario

# Seguro ya tenés registrado tu Post acá arriba:
admin.site.register(Post)

# 🔽 AGREGÁ ESTA LÍNEA ACÁ ABAJO 🔽
admin.site.register(Comentario)