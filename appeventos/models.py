
from django.db import models
from django.contrib.auth.models import User
from appcategorias.models import categorias



class eventosm(models.Model):
    tituloevento=models.CharField(max_length=120)
    contenidoevento=models.TextField()
    autorevento=models.ForeignKey(User,on_delete=models.CASCADE,related_name='eventosm')
    imagenevento=models.ImageField(default='logo.jpg',upload_to='eventos',null=True,blank=True)
    categoriaevento = models.ManyToManyField(categorias,related_name='categoriasevento',blank=True)
    eventolink = models.CharField(max_length=140)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tituloevento}'

    class Meta:
        verbose_name='eventosm'
        verbose_name_plural='eventosms'
        ordering=['created']
    
