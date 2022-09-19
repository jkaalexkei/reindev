# Generated by Django 3.2.4 on 2022-09-04 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appcategorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='eventosm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloevento', models.CharField(max_length=120, verbose_name='Titulo')),
                ('contenidoevento', models.TextField(verbose_name='Descripción del Evento')),
                ('imagenevento', models.ImageField(blank=True, default='logo.jpg', null=True, upload_to='eventos', verbose_name='Imagen del evento')),
                ('eventolink', models.CharField(max_length=200, verbose_name='Link evento')),
                ('fechaevento', models.DateField(verbose_name='Fecha del evento')),
                ('horaevento', models.TimeField(verbose_name='Hora del evento')),
                ('tipodeevento', models.CharField(choices=[('Presencial', 'Presencial'), ('Online', 'Online')], max_length=50, verbose_name='Tipo de Evento')),
                ('videoevento', models.FileField(max_length=200, upload_to='videos', verbose_name='Video del evento:')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('autorevento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventosm', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('categoriaevento', models.ManyToManyField(related_name='categoriasevento', to='appcategorias.categorias', verbose_name='Categorias')),
                ('subcategoriaevento', models.ManyToManyField(related_name='subcategoriasevento', to='appcategorias.subcategorias', verbose_name='Subcategorias')),
            ],
            options={
                'verbose_name': 'eventosm',
                'verbose_name_plural': 'eventosms',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='notificacioneseventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloeventos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificaciontituloeventos', to='appeventos.eventosm')),
            ],
            options={
                'verbose_name': 'notificacioneseventos',
                'verbose_name_plural': 'notificacioneseventoss',
            },
        ),
    ]
