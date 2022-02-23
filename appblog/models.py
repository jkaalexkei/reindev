from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class categorias(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    
    class Meta:
    
        verbose_name='categoria'
        verbose_name_plural='categorias'    
        

class blogm(models.Model):
    
    titulo=models.CharField(max_length=50)
    descripcion=models.TextField()
    imagen=models.ImageField(default='logo.jpg',upload_to='blogs',null=True,blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='blogms')#establece relacion entre el post y el usuario que crea el post
    categoria=models.ForeignKey(categorias,on_delete=models.CASCADE,null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:

        verbose_name='blogm'
        verbose_name_plural='blogms'
        ordering = ['-created']
    
    def __str__(self):
        return f'{self.user.username}:{self.content}'

    
