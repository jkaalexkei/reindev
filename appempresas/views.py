from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from appempresas.models import empresasm

from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login,logout
from reindev.forms import formcrearempresas

def empresasregistradas(request):
    empresas = empresasm.objects.all()
    contexto = {'empresas':empresas}
    return render(request,'appempresas/empresasregistradas.html',contexto)
    
def crearempresas(request):
    usuario = get_object_or_404(User,id = request.user.pk)
    if request.method == 'POST':
        formempresa = formcrearempresas(request.POST, request.FILES)
        if formempresa.is_valid():
            empresa = formempresa.save(commit=False)
            empresa.usuarioempresa = usuario
            empresa.save()
            messages.success(request,'Empresa Registrada con éxito')
            return redirect('home')
    else:
        formempresa = formcrearempresas()
    
    contexto = {'formempresa':formempresa}

    return render(request,'appempresas/crearempresas.html',contexto)