from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages

from appcategorias.models import categorias #importamos los modelos de la appcalendario
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login,logout
from reindev.forms import formcalendario

from appcalendario.models import calendariom
# from django.http import HttpResponseRedirect
# Create your views here.
# from proyecto_rein.forms import Inputimagen

def calendario(request):
    calendario = calendariom.objects.all()    

    contexto = {'calendarios':calendario}

    return render(request,'appcalendario/calendario.html',contexto)


def crearcalendario(request):
    usuario = get_object_or_404(User,pk=request.user.pk)
    
    if request.method == 'POST':
        # categoria = request.POST['categoriablog']
        # cat = categorias.objects.get(id=categoria)
        categoria = request.POST['categoriacalendario']
        formcalendarionuevo = formcalendario(request.POST,request.FILES)
        if formcalendarionuevo.is_valid():
            calendariof = formcalendarionuevo.save(commit=False)
            calendariof.autorcalendario = usuario            
            calendariof.save()
            calendariof.categoriacalendario.add(categoria)
            # blog.save()
            # print(categoria)
            messages.success(request,'Blog creado con éxito')
            
            return redirect('calendario')
    else:
        formcalendarionuevo = formcalendario()
    
    contexto = {'formcalendarionuevo':formcalendarionuevo}

    return render(request,'appcalendario/calendarionuevo.html',contexto)