# Generated by Django 3.2.4 on 2022-04-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcategorias', '0001_initial'),
        ('appeventos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventosm',
            name='categoriaevento',
        ),
        migrations.AddField(
            model_name='eventosm',
            name='categoriaevento',
            field=models.ManyToManyField(blank=True, null=True, related_name='categoriasevento', to='appcategorias.categorias'),
        ),
    ]
