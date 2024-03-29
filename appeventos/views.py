
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from .models import eventosm
from reindev.forms import registrareventosform,actualizareventosform
from appcomentarios.models import comentarioseventosm
from appusuario.models import usuariosm

# Create your views here.

def eventos(request):

    eventos = eventosm.objects.all()
    com = comentarioseventosm.objects.all()
    # c = 0
    # for e in eventos:
    #     for comentario in com:
    #         if comentario.comentariosevento_id == e.id:
    #             print(e.tituloevento)
    #             c= c+1
    # print(c)
    
    contexto = {'eventos':eventos,'comentarios':com}
    return render(request,'appeventos/eventos.html',contexto)



def crearevento(request):
    usuario = get_object_or_404(usuariosm,pk = request.user.pk)
    
    if request.method == 'POST':
        categoria = request.POST['categoriaevento']
        subcategoria = request.POST['subcategoriaevento']
        formevento = registrareventosform(request.POST,request.FILES)
        if formevento.is_valid():
            evento = formevento.save(commit=False)
            evento.autorevento = usuario
            evento.save()
            evento.categoriaevento.add(categoria)
            evento.subcategoriaevento.add(subcategoria)
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