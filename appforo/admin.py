from django.contrib import admin
from . models import categoria_foro,foro
# Register your models here.

class categoriaforoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class foroAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(categoria_foro,categoriaforoAdmin)
admin.site.register(foro,foroAdmin)


