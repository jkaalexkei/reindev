# Generated by Django 3.2.4 on 2022-09-24 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appempresas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biografia', models.CharField(default='Bienvenido a mi perfil', max_length=140)),
                ('imagenperfil', models.ImageField(blank=True, default='perfil/userdefault.jpg', null=True, upload_to='perfil')),
                ('puesto_cargo', models.CharField(max_length=140)),
                ('nombreempesauser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nombreempresauser', to='appempresas.empresasm', verbose_name='Elija la empresa:')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfils',
            },
        ),
    ]
