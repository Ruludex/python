from django import forms
from .models import Comentario
from .models import Perfil  # 👈 Asegurate de importar Perfil arriba si no lo está

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Dejá tu comentario acá...',
                'style': 'width: 100%; padding: 10px; border-radius: 6px; border: 1px solid #ced4da; resize: none;'
            }),
        }
        labels = {
            'contenido': '', # Quita la etiqueta automática "Contenido" para que se vea más limpio
        }
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto', 'biografia'] # Los dos campos que el usuario va a poder editar
        widgets = {
            'biografia': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Contanos algo sobre vos para tu perfil...',
                'style': 'width: 100%; padding: 10px; border-radius: 6px; border: 1px solid #ced4da; resize: none;'
            }),
            'foto': forms.ClearableFileInput(attrs={
                'style': 'margin-bottom: 15px;'
            }),
        }
        labels = {
            'foto': 'Foto de Perfil',
            'biografia': 'Biografía',
        }