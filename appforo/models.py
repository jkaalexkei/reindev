from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class categoria_forom(models.Model):
    nombre=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria_forom'
        verbose_name_plural='categoria_foroms'
    
    def __str__(self):
        return self.nombre

class forom(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.TextField()
    imagen=models.ImageField(default='logo.jpg', upload_to='foro')
    like=models.IntegerField(default=0)
    nolike=models.IntegerField(default=0)
    autorf=models.ForeignKey(User,on_delete=models.CASCADE,related_name='foroms')
    categoriasforo=models.ForeignKey(categoria_forom,on_delete=models.CASCADE,null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name='forom'
        verbose_name_plural='foroms'
        ordering = ['-created']

    def __str__(self):
        return f'{self.autorf.username}:{self.titulo}'

