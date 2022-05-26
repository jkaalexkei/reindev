from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views
# from apprein.formsold import crearcuentaform

urlpatterns = [

    path('',views.foro,name='foro'),
    path('agregarforo/',views.agregarforo,name='agregarforo'),
    path('busquedaforo/',views.busquedaforo.as_view(),name='busquedaforo'),
    path('editarforo/<id>',views.editarforo,name='editarforo'),
    path('eliminarforo/<id>',views.eliminarforo,name='eliminarforo'),
    path('descripcionforo/<pk>',views.mostrarforo.as_view(),name='mostrarforo'),

    

]

# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


