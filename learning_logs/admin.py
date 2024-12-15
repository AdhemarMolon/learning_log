from django.contrib import admin
from learning_logs.models import Topic, Entry, PerfilUsuario, Avaliacao, Comentario

# Configuração do admin para o modelo Topic
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('text',)
    date_hierarchy = 'date_added'

# Configuração do admin para o modelo Entry
@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text', 'date_added')
    list_filter = ('topic', 'date_added')
    search_fields = ('text', 'topic__text')
    date_hierarchy = 'date_added'

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