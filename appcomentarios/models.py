from django.db import models

from django.contrib.auth.models import User
from appblog.models import blogm
from appeventos.models import eventosm
from appforo.models import forom


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

class comentariosforom(models.Model):
    comentarioforo=models.CharField(max_length=140)
    autorcomentarioforo = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usersrelforo')
    comentariosfororel = models.ForeignKey(forom,on_delete=models.CASCADE,related_name='comentariosfororel',null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'comentariosforom'
        verbose_name_plural='comentariosforoms'
        ordering = ['-created']
    
    def __str__(self):
        return f'{self.comentarioforo}:{self.autorcomentarioforo}'