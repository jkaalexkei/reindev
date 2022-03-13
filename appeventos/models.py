from ast import AugStore
from pyexpat import model
from ssl import create_default_context
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class categoriaeventos(models.Model):
#     nombre=models.CharField(max_length=50)
#     created=models.DateTimeField(auto_now_add=True)
#     updated=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.nombre}'

# class eventosm(models.Model):
#     tituloevento=models.CharField(max_length=120,require=True)
#     contenidoevento=models.TextField()
#     autorevento=models.ForeignKey(User,on_delete=models.CASCADE,related_name='eventosm')
#     imagenevento=models.ImageField(default='logo.jpg',upload_to='eventos',null=True,blank=True)
#     created=models.DateTimeField(auto_now_add=True)
#     updated=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.user.username}:{self.tituloevento}'
    
