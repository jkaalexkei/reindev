from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views#importa desde la raiz las vistas


urlpatterns = [
    
    
    path('',views.blog, name='blog'),
    path('nuevaentrada/',views.registrarnuevaentrada,name='nuevaentrada')
   
    
]



