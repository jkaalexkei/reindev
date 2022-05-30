from django.contrib import admin
from .models import blogm,notificacionesblog #categorias#importamos el modelo de la appblog
# Register your models here.

# class categoriaadmin(admin.ModelAdmin):
#      readonly_fields=('created','updated')


class blogadmin(admin.ModelAdmin):
    readonly_fields=('created','updated')



admin.site.register(blogm, blogadmin)
admin.site.register(notificacionesblog)


