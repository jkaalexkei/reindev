from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    
    path('',views.home, name='home'),
    
    # path('foro/',views.foro, name='foro'),
    path('calendario/',views.calendario, name='calendario'),
    path('login/',views.iniciarsesion,name='login'),
    path('cerrarsesion/',views.cerrarsesion,name='logout'),
    path('crearcuenta/',views.crearcuenta,name='crearcuenta'),
    path('perfil/<str:usuario>',views.perfil,name='perfil'),
    path('editarperfil/',views.editarperfil,name='editarperfil')
    # path('',LoginView.as_view(template_name='apprein/login.html'),name='login'),
    # path('logout/',LogoutView.as_view(template_name='apprein/logout.html'),name='login'),
    
]
#Agregamos la url de las imagenes para indicarle al panel de administracion de django donde estan las imagenes
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

