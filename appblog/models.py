
# from django.db import models

# Create your models here.
from django.shortcuts import render
from django.db import models

from django.contrib.auth.models import User
from appcategorias.models import categorias

        
class blogm(models.Model):
    
    titulo=models.CharField(max_length=140)
    descripcion=models.TextField()
    imagen=models.ImageField(default='img/logo.jpg',upload_to='blogs',null=True,blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='blogms')#establece relacion entre el post y el usuario que crea el post
    categoria=models.ManyToManyField(categorias,related_name='categoriablogrel')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:

        verbose_name='blogm'
        verbose_name_plural='blogms'
        ordering = ['-created']
    
    def __str__(self):
        return f'{self.autor.username}:{self.titulo}'




    

    
