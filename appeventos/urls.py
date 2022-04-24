

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    
    path('',views.crearevento, name='crearevento'),
    path('eventos/',views.eventos,name="eventos")
    
]


