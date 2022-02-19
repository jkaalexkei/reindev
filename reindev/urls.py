"""proyecto_rein URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
# from django.urls.conf import include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('apprein/', include('apprein.urls')),
    path('', include('apprein.urls')),
    path('appblog/', include('appblog.urls')),
    path('appforo/', include('appforo.urls')),
    
    
    
       
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# https://www.youtube.com/watch?v=srOLTZYxMTc

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#pip install django-admin-interface 
#permite modificar la interfaz del admin de django

#https://pypi.org/project/django-admin-interface/ instalacion de django_interface