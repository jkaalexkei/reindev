from django.contrib import admin
from appforo.models import categoria_forom,forom
# Register your models here.

class categoriaforoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class foroAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(categoria_forom,categoriaforoAdmin)
admin.site.register(forom,foroAdmin)


