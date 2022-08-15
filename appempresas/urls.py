from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views#importa desde la raiz las vistas


urlpatterns = [
    
    path('crearempresa/',views.crearempresas, name='crearempresas'),
    path('empresasregistradas/',views.empresasregistradas,name="empresasregistradas"),
    path('eliminarempresa/<id>',views.eliminarempresa,name='eliminarempresa'),
    path('editarempresa/<id>/',views.editarempresa,name="editarempresa"),
    path('busquedaempresa/',views.busquedaempresa.as_view(),name='busquedaempresa'),
    path('descripcionempresa/<pk>',views.mostrarempresa.as_view(),name='mostrarempresa'),
    
    
    
]