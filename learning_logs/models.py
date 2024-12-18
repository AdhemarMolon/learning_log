
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Modelo que armazena informações adicionais sobre o perfil do usuário
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


# Modelo que representa uma avaliação feita pelo usuário
class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    nota = models.IntegerField(null=True, blank=True)
    data_avaliacao = models.DateTimeField(auto_now_add=True)
    tipo_refeicao = models.CharField(max_length=10, choices=[('almoço', 'Almoço'), ('jantar', 'Jantar')])

    def __str__(self):
        return f"{self.tipo_refeicao.capitalize()} - {self.texto[:50]}..." 


# Modelo que representa comentários específicos 
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)  # Renomeado para 'data'
    likes = models.ManyToManyField(User, related_name='comentario_likes')
    dislikes = models.ManyToManyField(User, related_name='comentario_dislikes')

    def __str__(self):
        return f"Comentário de {self.usuario.username} - {self.comentario[:50]}..."
