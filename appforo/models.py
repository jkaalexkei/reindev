from django.db import models
from django.contrib.auth.models import User
from appcategorias.models import categorias
# from appcategorias.models import categorias

# Create your models here.


class forom(models.Model):
    titulo=models.CharField(max_length=50,verbose_name='Titulo del foro:')
    contenido=models.TextField(verbose_name='Descripción del foro:')
    imagenforo=models.ImageField(default='logo.jpg', upload_to='foro',verbose_name='Imagen del foro:')
    autorforo=models.ForeignKey(User,on_delete=models.CASCADE,related_name='foroms', verbose_name='Autor del foro:')
    categoriasforo=models.ManyToManyField(categorias,related_name='categoriasforo',verbose_name='Categorias')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name='forom'
        verbose_name_plural='foroms'
        ordering = ['-created']

    def __str__(self):
        return f'{self.autorforo.username}:{self.titulo}'

