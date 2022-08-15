from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from appempresas.models import empresasm

from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login,logout
from reindev.forms import formcrearempresas,actualizarempresasform

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
            return redirect('empresasregistradas')
    else:
        formempresa = formcrearempresas()
    
    contexto = {'formempresa':formempresa}

    return render(request,'appempresas/crearempresas.html',contexto)


def editarempresa(request,id):

    e = empresasm.objects.get(id=id)
    empresa = get_object_or_404(empresasm,id=id)

    datos = {
        'empresa':e,
        'formempresa':actualizarempresasform(instance=empresa)
    }

    if request.method == 'POST':
        formulario = actualizarempresasform(data=request.POST,instance=empresa,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Información del empresa Actualizada')
            return redirect('empresasregistradas')
    else:
        formulario = actualizarempresasform()


    return render(request,'appempresas/modificarempresa.html',datos)

def eliminarempresa(request,id):
    empresa = empresasm.objects.get(id=id)
    empresa.delete()
    messages.success(request,'empresa Eliminado con éxito')
    return redirect ('empresasregistradas')


class mostrarempresa(DetailView):   
    
    model = empresasm

    template_name = 'appempresas/infoempresa.html'
    

     
    def get_context_data(self, **kwargs):

        context= super().get_context_data(**kwargs)
        # print(context)
        context['datosencontrados'] = context['empresasm']
        
       
        return context


class busquedaempresa(ListView):
     
     template_name = 'appempresas/busquedaempresa.html'

     def get_queryset(self):
          return empresasm.objects.filter(nombreempresa__icontains=self.query())
     
     def query(self):
          return self.request.GET.get('buscar') 
     
     def get_context_data(self, **kwargs):

          context= super().get_context_data(**kwargs)
          context['query'] = self.query()
          context['datosencontrados'] = context['empresasm_list']
          context['cantidad'] = context['empresasm_list'].count()
        #   context['miscategorias'] = categorias.objects.all()
          
        #   print(context)

          return context