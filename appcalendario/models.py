

from django.db import models
from django.contrib.auth.models import User
from appcategorias.models import categorias, subcategorias
# from django.db.models.signals import post_save
from appusuario.models import usuariosm


class calendariom(models.Model):
   
    titulocalendario=models.CharField(max_length=120,verbose_name='Titulo')
    # contenidocalendario=models.TextField(verbose_name='Descripción del calendario')
    autorcalendario=models.ForeignKey(usuariosm,on_delete=models.CASCADE,related_name='calendariosm',verbose_name='Autor')
    imagencalendario=models.ImageField(default='logo.png',upload_to='calendarios',null=True,blank=True,verbose_name='Imagen del calendario')
    categoriacalendario = models.ManyToManyField(categorias,related_name='categoriascalendario',verbose_name='Categorias')

    fechacalendario_dia = models.IntegerField(verbose_name='DIA')
    fechacalendario_mes = models.CharField(max_length=15,verbose_name='MES')
    fechacalendario_agno = models.IntegerField(verbose_name='AÑO')
    horacalendario = models.TimeField(auto_now=False,verbose_name='Hora del calendario')

    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.titulocalendario}:{self.autorcalendario.username}'

    class Meta:
        verbose_name='calendariosm'
        verbose_name_plural='calendariosms'
        ordering=['-created']
    
# class notificacionescalendarios(models.Model):
    
   
#     titulocalendarios = models.ForeignKey(calendariosm,on_delete=models.CASCADE,related_name='notificaciontitulocalendarios')

#     class Meta:
        
#         verbose_name='notificacionescalendarios'
#         verbose_name_plural='notificacionescalendarioss'
       

#     def __str__(self):
#         return f'{self.titulocalendarios}'    


# def crearnotificacioncalendarios(sender,instance,created,**kwargs):
    
#     if created:
#         notificacionescalendarios.objects.create(titulocalendarios=instance)

# post_save.connect(crearnotificacioncalendarios,sender=calendariosm)