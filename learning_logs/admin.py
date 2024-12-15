from django.contrib import admin
from learning_logs.models import PerfilUsuario, Avaliacao, Comentario


# Configuração do admin para o modelo PerfilUsuario
@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'data_nascimento')
    list_filter = ('data_nascimento',)
    search_fields = ('user__username', 'bio')
    date_hierarchy = 'data_nascimento'

# Configuração do admin para o modelo Avaliacao
@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo_refeicao', 'nota', 'data_avaliacao')
    list_filter = ('usuario', 'tipo_refeicao', 'data_avaliacao')
    search_fields = ('texto', 'usuario__username')
    date_hierarchy = 'data_avaliacao'

# Configuração do admin para o modelo Comentario
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'comentario', 'data')
    list_filter = ('usuario', 'data')
    search_fields = ('comentario', 'usuario__username')
    date_hierarchy = 'data'