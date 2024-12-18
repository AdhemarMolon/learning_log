# Generated by Django 5.1 on 2024-11-05 02:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0008_comentario_tipo_comentario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='tipo_comentario',
        ),
        migrations.AddField(
            model_name='comentario',
            name='dislikes',
            field=models.ManyToManyField(related_name='comentario_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentario',
            name='likes',
            field=models.ManyToManyField(related_name='comentario_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
