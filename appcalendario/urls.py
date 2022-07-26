from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views#importa desde la raiz las vistas


urlpatterns = [
    
    path('crearcalendario/',views.crearcalendario, name='crearcalendario'),
    path('calendario/',views.calendario,name="calendario"),
    # path('descripcionblog/<pk>',views.mostrarblog.as_view(),name='mostrarblog'),
    # path('eliminarblog/<id>',views.eliminarblog,name='eliminarblog'),
    # path('editarblog/<id>/',views.editarblog,name="editarblog"),
    # path('busquedablog/',views.busquedablog.as_view(),name='busquedablog'),
    
    
    
]