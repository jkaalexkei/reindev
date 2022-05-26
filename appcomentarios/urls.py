from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views
from appcomentarios.views import *


urlpatterns = [

    path('agregarcomentarioblog/<id>',views.agregarcomentarioblog,name='agregarcomentarioblog'),
    path('agregarcomentarioevento/<id>',views.agregarcomentarioeventos,name='agregarcomentarioeventos'),
    path('agregarcomentarioforo/<id>',views.agregarcomentarioforo,name='agregarcomentarioforo'),
   
]