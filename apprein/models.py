from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class perfil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    imagenperfil = models.ImageField(upload_to='foro',null=True,blank=True)
   
    class Meta:
        verbose_name='perfil'
        verbose_name_plural='perfils'
    
    