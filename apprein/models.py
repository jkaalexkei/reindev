
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.db.models.signals import post_save

from appempresas.models import empresasm
from appusuario.models import usuariosm
    

class perfil(models.Model):
    user = models.OneToOneField(usuariosm,on_delete=models.CASCADE)
    biografia = models.CharField(default='Bienvenido a mi perfil',max_length=140)
    imagenperfil = models.ImageField(default='perfil/userdefault.jpg', upload_to='perfil',null=True,blank=True)
    nombreempesauser = models.ForeignKey(empresasm,on_delete=models.CASCADE,related_name='nombreempresauser',null=True,blank=True, verbose_name='Elija la empresa:')
    puesto_cargo = models.CharField(max_length=140)
    class Meta:
        verbose_name='perfil'
        verbose_name_plural='perfils'
    
    def __str__(self):
        return f'Perfil de {self.user.username}'

def crearperfil(sender, instance,created, **kwargs):
    if created:
        perfil.objects.create(user = instance)

post_save.connect(crearperfil,sender=usuariosm)
    