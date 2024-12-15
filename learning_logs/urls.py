# App learning_log urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fila/', views.fila, name='fila'),    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
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
