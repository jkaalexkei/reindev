from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views
from appcategorias.views import *


urlpatterns = [

    path('',views.crearcategorias,name='crearcategorias'),
    path('listarcategorias/',listarcategorias.as_view(),name='listarcategorias'),
    path('mostrarcategorias/<pk>',views.mostrarcategorias.as_view(),name='mostrarcategorias'),
    path('actualizarcategorias/',views.actualizarcategorias,name='actualizacategorias'),
    path('eliminarcategoria/<id>',views.eliminarcategorias,name="eliminarcategorias")

]