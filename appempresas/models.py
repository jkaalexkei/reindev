from django.db import models

from django.contrib.auth.models import User

# from django.db.models.signals import post_save

class empresasm(models.Model):
    nombreempresa=models.CharField(max_length=120,verbose_name='Nombre')
    razonsocialempresa=models.TextField(verbose_name='Razon Social:')
    usuarioempresa=models.ForeignKey(User,on_delete=models.CASCADE,related_name='usuarioempresa',verbose_name='Usuario')
    correoempresa = models.CharField(max_length=120,verbose_name='Correo')
    imagenempresa = models.ImageField(default='logo.jpg',upload_to='empresa',null=True,blank=True,verbose_name='Imagen de la empresa')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
    
        verbose_name='empresasm'
        verbose_name_plural='empresasms'
        ordering = ['-created']
    
    def __str__(self):
        return f'{self.usuarioempresa.username}:{self.nombreempresa}'