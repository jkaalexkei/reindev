# Generated by Django 3.2.4 on 2022-09-20 03:06

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
            name='calendariom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulocalendario', models.CharField(max_length=120, verbose_name='Titulo')),
                ('imagencalendario', models.ImageField(blank=True, default='logo.png', null=True, upload_to='calendarios', verbose_name='Imagen del calendario')),
                ('fechacalendario_dia', models.IntegerField(verbose_name='DIA')),
                ('fechacalendario_mes', models.CharField(max_length=15, verbose_name='MES')),
                ('fechacalendario_agno', models.IntegerField(verbose_name='AÑO')),
                ('horacalendario', models.TimeField(verbose_name='Hora del calendario')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('autorcalendario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calendariosm', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('categoriacalendario', models.ManyToManyField(related_name='categoriascalendario', to='appcategorias.categorias', verbose_name='Categorias')),
            ],
            options={
                'verbose_name': 'calendariosm',
                'verbose_name_plural': 'calendariosms',
                'ordering': ['-created'],
            },
        ),
    ]
