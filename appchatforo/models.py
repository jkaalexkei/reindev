from django.db import models
from django.contrib.auth.models import User
from appforo.models import forom
from appusuario.models import usuariosm
# from appcategorias.models import categorias

# Create your models here.


class mensajechatforom(models.Model):
    mensaje=models.CharField(max_length=250,verbose_name='Mensaje')
    autormensaje=models.ForeignKey(usuariosm,on_delete=models.CASCADE,related_name='autormensajechat', verbose_name='Autor:')
    fororel=models.ForeignKey(forom,on_delete=models.CASCADE,related_name='fororel',verbose_name='Titulo foro')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name='mensajechatforom'
        verbose_name_plural='mensajechatforoms'
        ordering = ['-created']

    def __str__(self):
        return f'{self.autormensaje.username}:{self.mensaje}'

class respuestachatforom(models.Model):
    respuesta=models.CharField(max_length=250,verbose_name='Respuesta')
    autorrespuesta=models.ForeignKey(usuariosm,on_delete=models.CASCADE,related_name='autorrespuestachat', verbose_name='Autor:')
    mensajerelforo=models.ForeignKey(mensajechatforom,on_delete=models.CASCADE,related_name='mensajerelforo',verbose_name='Respuesta')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name='respuestachatforom'
        verbose_name_plural='respuestachatforoms'
        ordering = ['-created']

    def __str__(self):
        return f'{self.autorrespuesta.username}:{self.respuesta}'

