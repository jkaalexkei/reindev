
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from appcategorias.models import categorias, subcategorias
from django.db.models.signals import post_save



class eventosm(models.Model):
    opciones=[
        ('Presencial','Presencial'),
        ('Online','Online'),
    ]
    tituloevento=models.CharField(max_length=120,verbose_name='Titulo')
    contenidoevento=models.TextField(verbose_name='Descripción del Evento')
    autorevento=models.ForeignKey(User,on_delete=models.CASCADE,related_name='eventosm',verbose_name='Autor')
    imagenevento=models.ImageField(default='logo.jpg',upload_to='eventos',null=True,blank=True,verbose_name='Imagen del evento')
    categoriaevento = models.ManyToManyField(categorias,related_name='categoriasevento',verbose_name='Categorias')
    subcategoriaevento = models.ManyToManyField(subcategorias,related_name='subcategoriasevento',verbose_name='Subcategorias')
    eventolink = models.CharField(max_length=200,verbose_name='Link evento')
    fechaevento = models.DateField(verbose_name='Fecha del evento')
    horaevento = models.TimeField(auto_now=False,verbose_name='Hora del evento')

    tipodeevento = models.CharField(max_length=50,choices=opciones,verbose_name='Tipo de Evento')
    videoevento  = models.FileField(max_length=200,upload_to='videos',verbose_name='Video del evento:')
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