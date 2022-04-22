from django.contrib import admin
from .models import eventosm 
# Register your models here.



class eventosadmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(eventosm,eventosadmin)