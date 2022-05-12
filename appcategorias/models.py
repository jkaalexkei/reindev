from cProfile import label
from django.db import models

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

class subcategorias(models.Model):
    categoriarel=models.ForeignKey(categorias,on_delete=models.CASCADE,null=True,blank=True,related_name='categoriasrel',verbose_name='Categoria Principal')
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    
    class Meta:
    
        verbose_name='subcategoria'
        verbose_name_plural='subcategorias'
        ordering = ['-created']    
