from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views
from appcomentarios.views import *


urlpatterns = [

    path('agregarcomentarioblog/<id>',views.agregarcomentarioblog,name='agregarcomentarioblog'),
    path('agregarcomentarioevento/<id>',views.agregarcomentarioeventos,name='agregarcomentarioeventos'),
    # path('listarcategorias/',listarcategorias.as_view(),name='listarcategorias'),
    # path('mostrarcategorias/<pk>',views.mostrarcategorias.as_view(),name='mostrarcategorias'),
    # path('actualizarcategorias/',views.actualizarcategorias,name='actualizacategorias'),
    # path('eliminarcategoria/<id>',views.eliminarcategorias,name="eliminarcategorias"),
    # path('crearsubcategoria/',views.crearsubcategorias,name='crearsubcategorias'),
    # path('listarsubcategorias/<id>',views.listarsubcategorias,name="listarsubcategorias"),
]