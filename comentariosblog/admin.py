from django.contrib import admin
from comentariosblog.models import comentariosblogm

# Register your models here.

class comentariosadmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
admin.site.register(comentariosblogm,comentariosadmin)