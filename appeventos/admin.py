from django.contrib import admin
from .models import eventosm,notificacioneseventos 
# Register your models here.



class eventosadmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(eventosm,eventosadmin)
admin.site.register(notificacioneseventos)