from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views#importa desde la raiz las vistas


urlpatterns = [
    
    path('chatforo/<id>',views.chatforo, name='chatforo'),
    path('agregarmensaje/<id>',views.guardarmensajechatforo,name='agregarmensaje'),
    path('agregarrespuesta/<id>',views.guardarrespuestachatforo,name='agregarrespuesta'),
    
    
    
    
]

# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



