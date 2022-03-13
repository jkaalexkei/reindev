from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class perfil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    biografia = models.CharField(default='Bienvenido a mi perfil',max_length=140)
    imagenperfil = models.ImageField(default='perfil/userdefault.jpg', upload_to='perfil',null=True,blank=True)
   
    class Meta:
        verbose_name='perfil'
        verbose_name_plural='perfils'
    
    def __str__(self):
        return f'Perfil de {self.user.username}'

def crearperfil(sender, instance,created, **kwargs):
    if created:
        perfil.objects.create(user = instance)

post_save.connect(crearperfil,sender=User)
    