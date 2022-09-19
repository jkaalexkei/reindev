from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages

from appcategorias.models import categorias #importamos los modelos de la appcalendario
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login,logout
from reindev.forms import formcalendario,actualizarcalendariosform

from appcalendario.models import calendariom
from appusuario.models import usuariosm
# from django.http import HttpResponseRedirect
# Create your views here.
# from proyecto_rein.forms import Inputimagen

def calendario(request):
    calendario = calendariom.objects.all()    

    contexto = {'calendarios':calendario}

    return render(request,'appcalendario/calendario.html',contexto)


def crearcalendario(request):
    usuario = get_object_or_404(usuariosm,pk=request.user.pk)
    
    if request.method == 'POST':
        # categoria = request.POST['categoriacalendario']
        # cat = categorias.objects.get(id=categoria)
        categoria = request.POST['categoriacalendario']
        formcalendarionuevo = formcalendario(request.POST,request.FILES)
        if formcalendarionuevo.is_valid():
            calendariof = formcalendarionuevo.save(commit=False)
            calendariof.autorcalendario = usuario            
            calendariof.save()
            calendariof.categoriacalendario.add(categoria)
            # calendario.save()
            # print(categoria)
            messages.success(request,'calendario creado con éxito')
            
            return redirect('calendario')
    else:
        formcalendarionuevo = formcalendario()
    
    contexto = {'formcalendarionuevo':formcalendarionuevo}

    return render(request,'appcalendario/calendarionuevo.html',contexto)

class busquedacalendario(ListView):
     
     template_name = 'appcalendario/busquedacalendario.html'

     def get_queryset(self):
          return calendariom.objects.filter(titulocalendario__icontains=self.query())
     
     def query(self):
          return self.request.GET.get('buscar') 
     
     def get_context_data(self, **kwargs):

          context= super().get_context_data(**kwargs)
          context['query'] = self.query()
          context['datosencontrados'] = context['calendariom_list']
          context['cantidad'] = context['calendariom_list'].count()
        #   context['miscategorias'] = categorias.objects.all()
          
        #   print(context)

          return context

class busquedacalendariomes(ListView):
     
     template_name = 'appcalendario/busquedacalendario.html'

     def get_queryset(self):
          return calendariom.objects.filter(fechacalendario_mes__icontains=self.query())
     
     def query(self):
          return self.request.GET.get('buscar') 
     
     def get_context_data(self, **kwargs):

          context= super().get_context_data(**kwargs)
          context['querymes'] = self.query()
          context['datosencontrados'] = context['calendariom_list']
          context['cantidad'] = context['calendariom_list'].count()
        #   context['miscategorias'] = categorias.objects.all()
          
        #   print(context)

          return context

class busquedacalendarioagno(ListView):
     
     template_name = 'appcalendario/busquedacalendario.html'

     def get_queryset(self):
          return calendariom.objects.filter(fechacalendario_agno__icontains=self.query())
     
     def query(self):
          return self.request.GET.get('buscar') 
     
     def get_context_data(self, **kwargs):

          context= super().get_context_data(**kwargs)
          context['queryagno'] = self.query()
          context['datosencontrados'] = context['calendariom_list']
          context['cantidad'] = context['calendariom_list'].count()
        #   context['miscategorias'] = categorias.objects.all()
          
        #   print(context)

          return context


def editarcalendario(request,id):
    
    b = calendariom.objects.get(id=id)
    calendario = get_object_or_404(calendariom,id=id)

    datos = {
        'calendario':b,
        'formcalendario':actualizarcalendariosform(instance=calendario)
    }

    if request.method == 'POST':
        formulario = actualizarcalendariosform(data=request.POST,instance=calendario,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Información  Actualizada')
            return redirect('calendario')
    else:
        formulario = actualizarcalendariosform()


    return render(request,'appcalendario/modificarcalendario.html',datos)

def eliminarcalendario(request,id):
    calendario = calendariom.objects.get(id=id)
    calendario.delete()
    messages.success(request,'calendario Eliminado con éxito')
    return redirect ('calendario')

class mostrarcalendario(DetailView):
    
    
    
    model = calendariom

    template_name = 'appcalendario/articulocalendario.html'
    
    #  def get_queryset(self):
    #       return calendariom.objects.filter(titulo__icontains=self.query())
     
    #  def query(self):
    #       return self.request.GET.get('buscar') 
     
    def get_context_data(self, **kwargs):

        context= super().get_context_data(**kwargs)
        # print(context)
        context['datosencontrados'] = context['calendariom']
        # context['comentario'] = comentarioscalendariom.objects.all()
       
        return context