# Generated by Django 3.2.4 on 2022-05-12 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appcategorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategorias',
            name='categoriarel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoriasrel', to='appcategorias.categorias', verbose_name='Categoria Principal'),
        ),
    ]
