from django.db import models
from appblog.models import blogm
from django.contrib.auth.models import User


# Create your models here.

class comentariosblogm(models.Model):
    titulocomentario = models.CharField(max_length=140)
    comentario=models.CharField(max_length=140)
    entradablogs =models.ForeignKey(blogm,on_delete=models.CASCADE,related_name='blogms')
    autorcoment = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'comentariosblogm'
        verbose_name_plural='comentariosblogms'
        ordering = ['-created']
    
    def __str__(self):
        return f'{self.titulocomentario}:{self.autorcoment}'