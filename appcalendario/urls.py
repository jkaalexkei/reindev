from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views#importa desde la raiz las vistas


urlpatterns = [
    
    path('crearcalendario/',views.crearcalendario, name='crearcalendario'),
    path('calendario/',views.calendario,name="calendario"),
    path('descripcioncalendario/<pk>',views.mostrarcalendario.as_view(),name='mostrarcalendario'),
    path('eliminarcalendario/<id>',views.eliminarcalendario,name='eliminarcalendario'),
    path('editarcalendario/<id>/',views.editarcalendario,name="editarcalendario"),
    path('busquedacalendario/',views.busquedacalendario.as_view(),name='busquedacalendario'),
    path('busquedacalendariomes/',views.busquedacalendariomes.as_view(),name='busquedacalendariomes'),
     path('busquedacalendarioagno/',views.busquedacalendarioagno.as_view(),name='busquedacalendarioagno'),
    
    
    
]