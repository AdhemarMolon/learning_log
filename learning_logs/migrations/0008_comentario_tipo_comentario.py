# Generated by Django 5.1 on 2024-11-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0007_remove_comentario_dislikes_remove_comentario_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='tipo_comentario',
            field=models.CharField(choices=[('fila', 'Fila'), ('almoço', 'Almoço'), ('jantar', 'Jantar')], default='fila', max_length=10),
        ),
    ]