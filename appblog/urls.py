from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views#importa desde la raiz las vistas


urlpatterns = [
    
    
    path('',views.blog, name='blog'),
    path('nuevaentrada/',views.registrarnuevaentrada,name='nuevaentrada'),
    path('modificarentrada/',views.modificarentradablog,name='modificarentradablog'),
    path('articulo/<id>',views.vistaarticulocompleto,name='articuloblog')
   
    
]

# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



