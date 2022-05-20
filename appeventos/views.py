
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from .models import eventosm
from reindev.forms import registrareventosform,actualizareventosform
from appcomentarios.models import comentarioseventosm


# Create your views here.

def eventos(request):

    eventos = eventosm.objects.all()
    contexto = {'eventos':eventos}
    return render(request,'appeventos/eventos.html',contexto)



def crearevento(request):
    usuario = get_object_or_404(User,pk = request.user.pk)
    if request.method == 'POST':
        formevento = registrareventosform(request.POST,request.FILES)
        if formevento.is_valid():
            evento = formevento.save(commit=False)
            evento.autorevento = usuario
            evento.save()
            messages.success(request,'Evento creado con éxito')
            
            return redirect('eventos')
    else:
        formevento = registrareventosform()
    
    contexto = {'formevento':formevento}

    return render(request,'appeventos/crearevento.html',contexto)

def editarevento(request,id):

    e = eventosm.objects.get(id=id)
    evento = get_object_or_404(eventosm,id=id)

    datos = {
        'evento':e,
        'formevento':actualizareventosform(instance=evento)
    }

    if request.method == 'POST':
        formulario = actualizareventosform(data=request.POST,instance=evento,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Información del evento Actualizada')
            return redirect('eventos')
    else:
        formulario = actualizareventosform()


    return render(request,'appeventos/editarevento.html',datos)

def eliminareventos(request,id):
    evento = eventosm.objects.get(id=id)
    evento.delete()
    messages.success(request,'Evento Eliminado con éxito')
    return redirect ('eventos')


class mostrarevento(DetailView):
    
    model = eventosm

    template_name = 'appeventos/descripcionevento.html'

    #  def get_queryset(self):
    #       return eventosm.objects.filter(titulo__icontains=self.query())
     
    #  def query(self):
    #       return self.request.GET.get('buscar') 
     
    def get_context_data(self, **kwargs):

        context= super().get_context_data(**kwargs)
        # print(context)
        context['datosencontrados'] = context['eventosm']
        context['comentario'] = comentarioseventosm.objects.all()
       
        return context

class busquedaeventos(ListView):
     
     template_name = 'appeventos/busquedaeventos.html'

     def get_queryset(self):
          return eventosm.objects.filter(tituloevento__icontains=self.query())
     
     def query(self):
          return self.request.GET.get('buscar') 
     
     def get_context_data(self, **kwargs):

          context= super().get_context_data(**kwargs)
          context['query'] = self.query()
          context['datosencontrados'] = context['eventosm_list']
          context['cantidad'] = context['eventosm_list'].count()
        #   context['miscategorias'] = categorias.objects.all()
          
        #   print(context)

          return context