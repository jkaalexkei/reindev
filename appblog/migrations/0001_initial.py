# Generated by Django 3.2.4 on 2022-05-12 23:55

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
            name='blogm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=140)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, default='img/logo.jpg', null=True, upload_to='blogs')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogms', to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appcategorias.categorias')),
            ],
            options={
                'verbose_name': 'blogm',
                'verbose_name_plural': 'blogms',
                'ordering': ['-created'],
            },
        ),
    ]
