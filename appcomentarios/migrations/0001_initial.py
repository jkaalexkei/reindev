# Generated by Django 3.2.4 on 2022-09-24 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appforo', '0001_initial'),
        ('appeventos', '0001_initial'),
        ('appblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentariosforom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentarioforo', models.CharField(max_length=140)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('autorcomentarioforo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersrelforo', to=settings.AUTH_USER_MODEL)),
                ('comentariosfororel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentariosfororel', to='appforo.forom')),
            ],
            options={
                'verbose_name': 'comentariosforom',
                'verbose_name_plural': 'comentariosforoms',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='comentarioseventosm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentarioevento', models.CharField(max_length=140)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('autorcomentarioeventos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersrel', to=settings.AUTH_USER_MODEL)),
                ('comentariosevento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarioseventosrel', to='appeventos.eventosm')),
            ],
            options={
                'verbose_name': 'comentarioseventosm',
                'verbose_name_plural': 'comentarioseventosms',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='comentariosblogm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=140)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('autorcomentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
                ('comentariosblog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentariosblog', to='appblog.blogm')),
            ],
            options={
                'verbose_name': 'comentariosblogm',
                'verbose_name_plural': 'comentariosblogms',
                'ordering': ['-created'],
            },
        ),
    ]
