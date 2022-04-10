
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# from comentariosblog.models import comentariosblogm



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
        ordering = ['-created']    
        
# class comentariosblogm(models.Model):
#     comentario=models.CharField(max_length=140)
#     # autorcomentario = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='comentariosblogms')
#     tituloblog = models.ManyToManyField(blogm,blank=True,related_name='comentariosblogms')
#     created=models.DateTimeField(auto_now_add=True)
#     updated=models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name = 'comentariosblogm'
#         verbose_name_plural='comentariosblogms'
#         ordering = ['-created']
    
#     def __str__(self):
#         return f'{self.autorcomentario.username}'
        
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
        return f'{self.autor.username}:{self.titulo}'




    

    
