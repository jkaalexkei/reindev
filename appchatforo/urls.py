from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views#importa desde la raiz las vistas


urlpatterns = [
    
    path('chatforo/<id>',views.chatforo, name='chatforo'),
    path('agregarmensaje/<id>',views.guardarmensajechatforo,name='agregarmensaje'),
    path('editarmensaje/<id>',views.editarmensajechatforo,name="editarmensajechatforo"),
    path('eliminarmensaje/<id>',views.eliminarmensajechatforo,name="eliminarmensajechatforo"),

    path('agregarrespuesta/<id>',views.guardarrespuestachatforo,name='agregarrespuesta'),
    path('editarrespuesta/<id>',views.editarrespuestachatforo,name="editarrespuestachatforo"),
     
    
    
    
    
]

# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



