
# from django.db import models

# Create your models here.

from django.db import models

from django.contrib.auth.models import User
from appcategorias.models import categorias,subcategorias
from django.db.models.signals import post_save
from appusuario.models import usuariosm


        
class blogm(models.Model):
    
    tituloblog=models.CharField(max_length=120,verbose_name='Titulo')
    contenidoblog=models.TextField(verbose_name='Descripción del blog')
    autorblog=models.ForeignKey(usuariosm,on_delete=models.CASCADE,related_name='blogm',verbose_name='Autor')
    imagenblog=models.ImageField(default='logo.jpg',upload_to='blog',null=True,blank=True,verbose_name='Imagen del blog')
    categoriablog = models.ManyToManyField(categorias,related_name='categoriasblog',verbose_name='Categorias')
    subcategoriablog = models.ManyToManyField(subcategorias,related_name='subcategoriasblog',verbose_name='Subcategorias')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
    
        verbose_name='blogm'
        verbose_name_plural='blogms'
        ordering = ['-created']
    
    def __str__(self):
        return f'{self.autorblog.username}:{self.tituloblog}'

class notificacionesblog(models.Model):
    
   
    tituloblog = models.ForeignKey(blogm,on_delete=models.CASCADE,related_name='notificaciontituloblog')

    class Meta:
        
        verbose_name='notificacionesblog'
        verbose_name_plural='notificacionesblogs'
       

    def __str__(self):
        return f'{self.tituloblog}'    


def crearnotificacionblog(sender,instance,created,**kwargs):
    
    if created:
        notificacionesblog.objects.create(tituloblog=instance)

post_save.connect(crearnotificacionblog,sender=blogm)

    




    

    
