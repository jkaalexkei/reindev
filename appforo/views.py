from django.shortcuts import render
from appforo.models import foro,categoria_foro

# Create your views here.

def foro(request):

    foropublicacion=foro.objects.all()
    categoriaforo=categoria_foro.objects.get(id='1')
    entradaforo = foro.objects.filter(categoriasforo=categoriaforo)
    


    return render(request,"appforo/foro.html",{
        'foro':foropublicacion,
        'categoria':entradaforo}
    )