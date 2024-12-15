from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry, Avaliacao, Comentario
from .forms import TopicForm, EntryForm, ComentarioForm, AvaliacaoForm
from django.db.models import Avg
from math import ceil

def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    return render(request, 'learning_logs/topics.html', {'topics': topics})

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    return render(request, 'learning_logs/topic.html', {'topic': topic, 'entries': entries})

#@login_required
def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('topics')
    else:
        form = TopicForm()
    return render(request, 'learning_logs/new_topic.html', {'form': form})

#@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.topic = topic
            entry.save()
            return redirect('topic', topic_id=topic_id)
    else:
        form = EntryForm()
    return render(request, 'learning_logs/new_entry.html', {'topic': topic, 'form': form})

#@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('topic', topic_id=topic.id)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'learning_logs/edit_entry.html', {'entry': entry, 'topic': topic, 'form': form})

#@login_required
def fila(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.save()
            return redirect('fila')  
    else:
        form = ComentarioForm()
    
    comentarios = Comentario.objects.all()
    
    context = {
        'form': form,
        'comentarios': comentarios,
    }
    return render(request, 'learning_logs/fila.html', context)

#@login_required
def almoço(request):
    if request.method == 'POST':
        nota = request.POST.get('nota')
        comentario_texto = request.POST.get('comentario')
        if nota and comentario_texto:
            avaliacao = Avaliacao(
                usuario=request.user,
                tipo_refeicao='almoço',
                nota=int(nota),
                texto=comentario_texto
            )
            avaliacao.save()
            return redirect('almoço')
    # Calcula a média das avaliações para 'almoço'
    lunch_rating = Avaliacao.objects.filter(tipo_refeicao='almoço', nota__isnull=False).aggregate(Avg('nota'))['nota__avg'] or 0
    lunch_comments = Avaliacao.objects.filter(tipo_refeicao='almoço').order_by('-data_avaliacao')

    context = {
        'lunch_rating': lunch_rating,
        'lunch_comments': lunch_comments,
    }
    return render(request, 'learning_logs/almoço.html', context)

#@login_required
def jantar(request):
    if request.method == 'POST':
        nota = request.POST.get('nota')
        comentario_texto = request.POST.get('comentario')
        if nota and comentario_texto:
            avaliacao = Avaliacao(
                usuario=request.user,
                tipo_refeicao='jantar',
                nota=int(nota),
                texto=comentario_texto
            )
            avaliacao.save()
            return redirect('jantar')
    # Calcula a média das avaliações para 'jantar'
    dinner_rating = Avaliacao.objects.filter(tipo_refeicao='jantar', nota__isnull=False).aggregate(Avg('nota'))['nota__avg'] or 0
    dinner_comments = Avaliacao.objects.filter(tipo_refeicao='jantar').order_by('-data_avaliacao')

    context = {
        'dinner_rating': dinner_rating,
        'dinner_comments': dinner_comments,
    }
    return render(request, 'learning_logs/jantar.html', context)

def perfil(request):
    return render(request, 'learning_logs/perfil.html')

def avaliacoes(request):
    avaliacoes = Avaliacao.objects.all()
    lunch_rating = avaliacoes.filter(tipo_refeicao='almoço').aggregate(Avg('nota'))['nota__avg']
    dinner_rating = avaliacoes.filter(tipo_refeicao='jantar').aggregate(Avg('nota'))['nota__avg']
    lunch_comments = avaliacoes.filter(tipo_refeicao='almoço')
    dinner_comments = avaliacoes.filter(tipo_refeicao='jantar')
    queue_comments = Comentario.objects.all()

    context = {
        'avaliacoes': avaliacoes,
        'lunch_rating': lunch_rating,
        'dinner_rating': dinner_rating,
        'lunch_comments': lunch_comments,
        'dinner_comments': dinner_comments,
        'queue_comments': queue_comments,
    }
    return render(request, 'learning_logs/avaliacoes.html', context)

#@login_required
def like_comentario(request, comentario_id):
    try:
        comentario = Comentario.objects.get(id=comentario_id)
        comentario.likes.add(request.user)
    except Comentario.DoesNotExist:
        return redirect('avaliacoes')
    return redirect('avaliacoes')

#@login_required
def dislike_comentario(request, comentario_id):
    try:
        comentario = Comentario.objects.get(id=comentario_id)
        comentario.dislikes.add(request.user)
    except Comentario.DoesNotExist:
        return redirect('avaliacoes')
    return redirect('avaliacoes')

#@login_required
def remover_like_comentario(request, comentario_id):
    try:
        comentario = Comentario.objects.get(id=comentario_id)
        comentario.likes.remove(request.user)
    except Comentario.DoesNotExist:
        return redirect('avaliacoes')
    return redirect('avaliacoes')

#@login_required
def remover_dislike_comentario(request, comentario_id):
    try:
        comentario = Comentario.objects.get(id=comentario_id)
        comentario.dislikes.remove(request.user)
    except Comentario.DoesNotExist:
        return redirect('avaliacoes')
    return redirect('avaliacoes')

#@login_required
def novo_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.save()
            return redirect('avaliacoes')
    else:
        form = ComentarioForm()
    return render(request, 'learning_logs/novo_comentario.html', {'form': form})

def listar_comentarios(request):
    comentarios = Comentario.objects.all()
    context = {'comentarios': comentarios}
    return render(request, 'learning_logs/listar_comentarios.html', context)

#@login_required
def editar_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('listar_comentarios')
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'learning_logs/editar_comentario.html', {'form': form, 'comentario': comentario})

#@login_required
def excluir_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    comentario.delete()
    return redirect('listar_comentarios')

#@login_required
def avaliar_almoço(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.usuario = request.user
            avaliacao.tipo_refeicao = 'almoço'
            avaliacao.save()
            return redirect('almoço')
    else:
        form = AvaliacaoForm()
    return render(request, 'learning_logs/avaliar_almoço.html', {'form': form})

#@login_required
def avaliar_jantar(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.usuario = request.user
            avaliacao.tipo_refeicao = 'jantar'
            avaliacao.save()
            return redirect('jantar')
    else:
        form = AvaliacaoForm()
    return render(request, 'learning_logs/avaliar_jantar.html', {'form': form})

#@login_required
def editar_avaliacao(request, avaliacao_id):
    avaliacao = Avaliacao.objects.get(id=avaliacao_id)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect('avaliacoes')
    else:
        form = AvaliacaoForm(instance=avaliacao)
    return render(request, 'learning_logs/editar_avaliacao.html', {'form': form, 'avaliacao': avaliacao})

#@login_required
def excluir_avaliacao(request, avaliacao_id):
    avaliacao = Avaliacao.objects.get(id=avaliacao_id)
    if request.method == 'POST':
        avaliacao.delete()
        return redirect('avaliacoes')
    return render(request, 'learning_logs/excluir_avaliacao.html', {'avaliacao': avaliacao})

def detalhar_avaliacao(request, avaliacao_id):
    avaliacao = Avaliacao.objects.get(id=avaliacao_id)
    context = {'avaliacao': avaliacao}
    return render(request, 'learning_logs/detalhar_avaliacao.html', context)

#@login_required
def listar_avaliacoes_usuario(request):
    avaliacoes = Avaliacao.objects.filter(usuario=request.user)
    context = {'avaliacoes': avaliacoes}
    return render(request, 'learning_logs/listar_avaliacoes_usuario.html', context)

def estatisticas_avaliacoes(request):
    total_avaliacoes = Avaliacao.objects.count()
    media_avaliacoes = Avaliacao.objects.aggregate(Avg('nota'))['nota__avg']
    avaliacoes_almoco = Avaliacao.objects.filter(tipo_refeicao='almoço').count()
    avaliacoes_jantar = Avaliacao.objects.filter(tipo_refeicao='jantar').count()

    context = {
        'total_avaliacoes': total_avaliacoes,
        'media_avaliacoes': media_avaliacoes,
        'avaliacoes_almoco': avaliacoes_almoco,
        'avaliacoes_jantar': avaliacoes_jantar,
    }
    return render(request, 'learning_logs/estatisticas_avaliacoes.html', context)