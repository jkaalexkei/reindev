from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views
from apprein.forms import crearcuentaform

urlpatterns = [

    path('',views.foro,name='foro'),
    path('crearforo/',views.crearforo,name='crearforo'),
    path('modificarforo/<id>',views.modificarentradaforo,name='modificarentradaforo'),

]

# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


