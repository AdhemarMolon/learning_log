from django import forms
from .models import Topic, Entry, Avaliacao, Comentario

# Formulário para o modelo Topic
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic  # Especifica o modelo associado a este formulário
        fields = ('text',)  # Campos do modelo que serão incluídos no formulário
        labels = {
            'text': 'Título do Tópico',  # Rótulo personalizado para o campo 'text'
        }
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'})  # Widget personalizado para o campo 'text'
        }

# Formulário para o modelo Entry
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry  # Especifica o modelo associado a este formulário
        fields = ('text',)  # Campos do modelo que serão incluídos no formulário
        labels = {
            'text': 'Texto da Entrada',  # Rótulo personalizado para o campo 'text'
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'})  # Widget personalizado para o campo 'text'
        }

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