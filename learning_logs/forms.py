from django import forms
from .models import Avaliacao, Comentario


# Formulário para o modelo Avaliacao
class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao  # Especifica o modelo associado a este formulário
        fields = ('nota', 'texto')  # Campos do modelo que serão incluídos no formulário
        labels = {
            'nota': 'Nota (de 1 a 5)',  # Rótulo personalizado para o campo 'nota'
            'texto': 'Comentário',  # Rótulo personalizado para o campo 'texto'
        }
        widgets = {
            'nota': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),  # Widget personalizado para o campo 'nota'
            'texto': forms.Textarea(attrs={'class': 'form-control'})  # Widget personalizado para o campo 'texto'
        }

# Formulário para o modelo Comentario
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario  # Especifica o modelo associado a este formulário
        fields = ('comentario',)  # Campos do modelo que serão incluídos no formulário
        labels = {
            'comentario': 'Deixe seu comentário aqui...',  # Rótulo personalizado para o campo 'comentario'
        }
        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})  # Widget personalizado para o campo 'comentario'
        }