# Generated by Django 3.2.4 on 2022-09-24 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appcategorias', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blogm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloblog', models.CharField(max_length=120, verbose_name='Titulo')),
                ('contenidoblog', models.TextField(verbose_name='Descripción del blog')),
                ('imagenblog', models.ImageField(blank=True, default='blog/logo.png', null=True, upload_to='blog', verbose_name='Imagen del blog')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('autorblog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogm', to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('categoriablog', models.ManyToManyField(related_name='categoriasblog', to='appcategorias.categorias', verbose_name='Categorias')),
                ('subcategoriablog', models.ManyToManyField(related_name='subcategoriasblog', to='appcategorias.subcategorias', verbose_name='Subcategorias')),
            ],
            options={
                'verbose_name': 'blogm',
                'verbose_name_plural': 'blogms',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='notificacionesblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloblog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificaciontituloblog', to='appblog.blogm')),
            ],
            options={
                'verbose_name': 'notificacionesblog',
                'verbose_name_plural': 'notificacionesblogs',
            },
        ),
    ]
