
# from django.db import models

# Create your models here.

from django.db import models

from django.contrib.auth.models import User
from appcategorias.models import categorias

        
class blogm(models.Model):
    
    tituloblog=models.CharField(max_length=120,verbose_name='Titulo')
    contenidoblog=models.TextField(verbose_name='Descripción del blog')
    autorblog=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blogm',verbose_name='Autor')
    imagenblog=models.ImageField(default='logo.jpg',upload_to='blog',null=True,blank=True,verbose_name='Imagen del blog')
    categoriablog = models.ManyToManyField(categorias,related_name='categoriasblog',verbose_name='Categorias')
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
    
        verbose_name='blogm'
        verbose_name_plural='blogms'
        ordering = ['-created']
    
    def __str__(self):
        return f'{self.autorblog.username}:{self.tituloblog}'
    
    # titulo=models.CharField(max_length=140)
    # descripcion=models.TextField()
    # imagen=models.ImageField(default='img/logo.jpg',upload_to='blogs',null=True,blank=True)
    # autor=models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='blogms')#establece relacion entre el post y el usuario que crea el post
    # categoriablog = models.ManyToManyField(categorias,related_name='categoriasblog',verbose_name='Categorias')
    # created=models.DateTimeField(auto_now_add=True)
    # updated=models.DateTimeField(auto_now_add=True)


    




    

    
