# App learning_log urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('fila/', views.fila, name='fila'),
    path('almoço/', views.almoço, name='almoço'),
    path('jantar/', views.jantar, name='jantar'),
    path('perfil/', views.perfil, name='perfil'),
    path('avaliacoes/', views.avaliacoes, name='avaliacoes'),
    path('avaliar_almoço/', views.avaliar_almoço, name='avaliar_almoço'),
    path('avaliar_jantar/', views.avaliar_jantar, name='avaliar_jantar'),
    path('editar_avaliacao/<int:avaliacao_id>/', views.editar_avaliacao, name='editar_avaliacao'),
    path('excluir_avaliacao/<int:avaliacao_id>/', views.excluir_avaliacao, name='excluir_avaliacao'),
    path('detalhar_avaliacao/<int:avaliacao_id>/', views.detalhar_avaliacao, name='detalhar_avaliacao'),
    path('minhas_avaliacoes/', views.listar_avaliacoes_usuario, name='minhas_avaliacoes'),
    path('estatisticas_avaliacoes/', views.estatisticas_avaliacoes, name='estatisticas_avaliacoes'),
    path('novo_comentario/', views.novo_comentario, name='novo_comentario'),

]
