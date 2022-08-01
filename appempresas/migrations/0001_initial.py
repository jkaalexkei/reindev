# Generated by Django 3.2.4 on 2022-08-01 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='empresasm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreempresa', models.CharField(max_length=120, verbose_name='Nombre')),
                ('razonsocialempresa', models.TextField(verbose_name='Razon Social:')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('usuarioempresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarioempresa', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'empresasm',
                'verbose_name_plural': 'empresasms',
                'ordering': ['-created'],
            },
        ),
    ]
