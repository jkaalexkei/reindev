from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views#importa desde la raiz las vistas
from appblog.views import busquedaarticulos

urlpatterns = [
    
    
    path('',views.blog, name='blog'),
    path('nuevaentrada/',views.registrarnuevaentrada,name='nuevaentrada'),
    path('modificarentrada/<id>',views.modificarentradablog,name='modificarentradablog'),
    path('articulo/<id>',views.vistaarticulocompleto,name='articuloblog'),
    path('eliminararticulo/<id>',views.eliminararticulo,name='eliminararticulo'),
    path('registrarcomentarios/',views.guardarcomentario,name='registrarcomentarios'),
    path('busquedablog/',busquedaarticulos.as_view(),name='buscar'),
    
    
    
]

# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



