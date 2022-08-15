from django.db import models
from django.contrib.auth.models import User
from appcategorias.models import categorias,subcategorias
from django.db.models.signals import post_save
# from appcategorias.models import categorias

# Create your models here.


class forom(models.Model):
    tituloforo=models.CharField(max_length=50,verbose_name='Titulo del foro:')
    contenidoforo=models.TextField(verbose_name='Descripción del foro:')
    imagenforo=models.ImageField(default='img/logo.jpg', upload_to='foro',verbose_name='Imagen del foro:')
    autorforo=models.ForeignKey(User,on_delete=models.CASCADE,related_name='foroms', verbose_name='Autor del foro:')
    categoriasforo=models.ManyToManyField(categorias,related_name='categoriasforo',verbose_name='Categorias')
    subcategoriasforo=models.ManyToManyField(subcategorias,related_name='subcategoriasforo',verbose_name='Subategorias')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name='forom'
        verbose_name_plural='foroms'
        ordering = ['-created']

    def __str__(self):
        return f'{self.autorforo.username}:{self.tituloforo}'

class notificacionesforo(models.Model):
    
   
    tituloforo = models.ForeignKey(forom,on_delete=models.CASCADE,related_name='notificaciontituloforo')

    class Meta:
        
        verbose_name='notificacionesforo'
        verbose_name_plural='notificacionesforos'
       

    def __str__(self):
        return f'{self.tituloforo}'    


def crearnotificacionforo(sender,instance,created,**kwargs):
    
    if created:
        notificacionesforo.objects.create(tituloforo=instance)

post_save.connect(crearnotificacionforo,sender=forom)