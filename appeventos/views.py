from django.shortcuts import render

from .models import eventosm
from reindev.forms import registrareventosform
# Create your views here.



def crearevento(request):

    formevento = registrareventosform()

    contexto = {'formevento':formevento}

    return render(request,'appeventos/crearevento.html',contexto)