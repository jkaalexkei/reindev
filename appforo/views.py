from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
 #importamos los modelos de la appblog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from appforo.models import forom
from appforo.models import categoria_foro

# Create your views here.

def foro(request):

    foropublicacion=forom.objects.all()
    categoriaforo=categoria_foro.objects.get(id='1')
    entradaforo = forom.objects.filter(categoriasforo=categoriaforo)
    


    return render(request,"appforo/foro.html",{
        'foro':foropublicacion,
        'categoria':entradaforo}
    )