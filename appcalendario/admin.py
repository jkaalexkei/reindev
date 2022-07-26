from django.contrib import admin
from .models import calendariom

class calendarioadmin(admin.ModelAdmin):
    readonly_fields=('created','updated')



admin.site.register(calendariom, calendarioadmin)
