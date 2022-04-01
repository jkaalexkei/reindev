# Generated by Django 3.2.4 on 2022-03-29 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentariosblogm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulocomentario', models.CharField(max_length=140)),
                ('comentario', models.CharField(max_length=140)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('entradablogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogms', to='appblog.blogm')),
            ],
            options={
                'verbose_name': 'comentariosblogm',
                'verbose_name_plural': 'comentariosblogms',
                'ordering': ['-created'],
            },
        ),
    ]
