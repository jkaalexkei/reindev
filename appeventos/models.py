
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from appcategorias.models import categorias, subcategorias
from django.db.models.signals import post_save
from appusuario.models import usuariosm



class eventosm(models.Model):
    opciones=[
        ('Presencial','Presencial'),
        ('Online','Online'),
    ]
    tituloevento=models.CharField(max_length=120,verbose_name='Titulo')
    contenidoevento=models.TextField(verbose_name='Descripción del Evento')
    autorevento=models.ForeignKey(usuariosm,on_delete=models.CASCADE,related_name='eventosm',verbose_name='Autor')
    imagenevento=models.ImageField(default='eventos/logo.png',upload_to='eventos',verbose_name='Imagen del evento',null=True, blank=True)
    categoriaevento = models.ManyToManyField(categorias,related_name='categoriasevento',verbose_name='Categorias')
    subcategoriaevento = models.ManyToManyField(subcategorias,related_name='subcategoriasevento',verbose_name='Subcategorias')
    eventolink = models.CharField(max_length=200,verbose_name='Link evento',null=True, blank=True)
    fechaevento = models.DateField(verbose_name='Fecha del evento')
    horaevento = models.TimeField(auto_now=False,verbose_name='Hora del evento')

    tipodeevento = models.CharField(max_length=50,choices=opciones,verbose_name='Tipo de Evento')
    # videoevento  = models.FileField(max_length=200,upload_to='archivos',verbose_name='Video del evento:', null=True, blank=True)
    archivoevento  = models.FileField(max_length=500,upload_to='archivos',verbose_name='Archivo del evento:', null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tituloevento}:{self.autorevento.username}'

    class Meta:
        verbose_name='eventosm'
        verbose_name_plural='eventosms'
        ordering=['-created']
    
class notificacioneseventos(models.Model):
    
   
    tituloeventos = models.ForeignKey(eventosm,on_delete=models.CASCADE,related_name='notificaciontituloeventos')

    class Meta:
        
        verbose_name='notificacioneseventos'
        verbose_name_plural='notificacioneseventoss'
       

    def __str__(self):
        return f'{self.tituloeventos}'    


def crearnotificacioneventos(sender,instance,created,**kwargs):
    
    if created:
        notificacioneseventos.objects.create(tituloeventos=instance)

post_save.connect(crearnotificacioneventos,sender=eventosm)