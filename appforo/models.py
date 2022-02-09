from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class categoria_foro(models.Model):
    nombre=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria_foro'
        verbose_name_plural='categoria_foros'
    
    def __str__(self):
        return self.nombre

class foro(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.TextField()
    imagen=models.ImageField(upload_to='foro',null=True,blank=True)
    like=models.IntegerField()
    nolike=models.IntegerField()
    autor=models.ForeignKey(User,on_delete=models.CASCADE)
    categoriasforo=models.ManyToManyField(categoria_foro)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name='foro'
        verbose_name_plural='foros'

    def __str__(self):
        return self.titulo

