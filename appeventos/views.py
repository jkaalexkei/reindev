from email import message
from pyexpat import model
from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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
            
            return redirect('eventos')
    else:
        formevento = registrareventosform()
    
    contexto = {'formevento':formevento}

    return render(request,'appeventos/crearevento.html',contexto)

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
       
        return context

class busquedaarticulos(ListView):
     
     template_name = 'appblog/busquedaeventos.html'

     def get_queryset(self):
          return eventosm.objects.filter(tituloevento__icontains=self.query())
     
     def query(self):
          return self.request.GET.get('buscar') 
     
     def get_context_data(self, **kwargs):

          context= super().get_context_data(**kwargs)
          context['query'] = self.query()
          context['datosencontrados'] = context['object_list']
          context['cantidad'] = context['object_list'].count()
        #   context['miscategorias'] = categorias.objects.all()


          return context