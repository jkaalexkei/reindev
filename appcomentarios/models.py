from django.db import models

from django.contrib.auth.models import User
from appblog.models import blogm
from appeventos.models import eventosm


# Create your models here.

class comentariosblogm(models.Model):
    comentario=models.CharField(max_length=140)
    autorcomentario = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    comentariosblog = models.ForeignKey(blogm,on_delete=models.CASCADE,related_name='comentariosblog',null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'comentariosblogm'
        verbose_name_plural='comentariosblogms'
        ordering = ['-created']
    
    def __str__(self):
        return f'{self.comentario}:{self.autorcomentario}'


class comentarioseventosm(models.Model):
    comentarioevento=models.CharField(max_length=140)
    autorcomentarioeventos = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usersrel')
    comentariosevento = models.ForeignKey(eventosm,on_delete=models.CASCADE,related_name='comentarioseventosrel',null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'comentarioseventosm'
        verbose_name_plural='comentarioseventosms'
        ordering = ['-created']
    
    def __str__(self):
        return f'{self.comentariosevento}:{self.autorcomentarioeventos}'