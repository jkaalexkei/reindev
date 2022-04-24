from email import message
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import eventosm
from reindev.forms import registrareventosform
# Create your views here.

def eventos(request):
    eventos = eventosm.objects.all()
    contexto = {'eventos':eventos}
    return render(request,'appeventos/eventos.html',contexto)

def crearevento(request):

    if request.method == 'POST':
        formevento = registrareventosform(request.POST,request.FILES)
        if formevento.is_valid():
            formevento.save()
            messages.success(request,'Evento creado con éxito')
            
            return redirect('home')
    else:
        formevento = registrareventosform()
    
    contexto = {'formevento':formevento}

    return render(request,'appeventos/crearevento.html',contexto)