# Generated by Django 3.2.4 on 2022-07-30 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appforo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='mensajechatforom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=250, verbose_name='Mensaje')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('autormensaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autormensajechat', to=settings.AUTH_USER_MODEL, verbose_name='Autor:')),
                ('fororel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fororel', to='appforo.forom', verbose_name='Titulo foro')),
            ],
            options={
                'verbose_name': 'mensajechatforom',
                'verbose_name_plural': 'mensajechatforoms',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='respuestachatforom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.CharField(max_length=250, verbose_name='Respuesta')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('autorrespuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autorrespuestachat', to=settings.AUTH_USER_MODEL, verbose_name='Autor:')),
                ('mensajerelforo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajerelforo', to='appchatforo.mensajechatforom', verbose_name='Respuesta')),
            ],
            options={
                'verbose_name': 'respuestachatforom',
                'verbose_name_plural': 'respuestachatforoms',
                'ordering': ['-created'],
            },
        ),
    ]
