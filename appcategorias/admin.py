from django.contrib import admin
from appcategorias.models import categorias, subcategorias

# Register your models here.
class categoriaadmin(admin.ModelAdmin):
     readonly_fields=('created','updated')

admin.site.register(categorias,categoriaadmin)
admin.site.register(subcategorias)