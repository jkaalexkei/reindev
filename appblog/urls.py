from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views#importa desde la raiz las vistas


urlpatterns = [
    
    path('crearblog/',views.crearblog, name='crearblog'),
    path('blog/',views.blog,name="blog"),
    path('descripcionblog/<pk>',views.mostrarblog.as_view(),name='mostrarblog'),
    path('eliminarblog/<id>',views.eliminarblog,name='eliminarblog'),
    path('editarblog/<id>/',views.editarblog,name="editarblog"),
    path('busquedablog/',views.busquedablog.as_view(),name='busquedablog'),
    
    
    
]

# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



