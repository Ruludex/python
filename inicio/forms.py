from django import forms
from .models import Comentario

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