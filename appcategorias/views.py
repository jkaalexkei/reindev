from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from reindev.forms import crearcategoriasform
from .models import categorias
# Create your views here.

def actualizarcategorias(request):
     if request.method == 'POST':
          idcategoria =request.POST['idcategoria']
          nombrecategoria = request.POST['nombrecategoria']
          bcategoria = categorias.objects.filter(id = idcategoria).exists()
          if bcategoria:
               cat = categorias.objects.get(id = idcategoria)
               cat.nombre = nombrecategoria
               cat.save()
               messages.success(request,'Categoria Actualizada')
               return redirect('listarcategorias')
               
          # else:
          #      nuevacategoria = categorias.objects.create(nombre=nombrecategoria)
          #      if nuevacategoria:
          #           nuevacategoria.save()
          #           messages.success(request,'Categoria creada satisfactoriamente')
          #           return redirect('home')
          #      else:
          #           messages.error(request,'error')
     return render(request,'appcategorias/listarcategorias.html',{})

def crearcategorias(request):
    
     if request.method == 'POST':
          nombrecategoria = request.POST['nombrecategoria']
          buscarcategoria = categorias.objects.filter(nombre = nombrecategoria).exists()
          if buscarcategoria:
               cat = categorias.objects.get(nombre = nombrecategoria)
               # cat.nombre = nombrecategoria
               # cat.save()
               messages.warning(request,'Categoria ya existe')
               return redirect('listarcategorias')
               
          else:
               nuevacategoria = categorias.objects.create(nombre=nombrecategoria)
               if nuevacategoria:
                    nuevacategoria.save()
                    messages.success(request,'Categoria creada satisfactoriamente')
                    return redirect('listarcategorias')
               else:
                    messages.error(request,'error')

     return render(request,'appcategorias/categorias.html')



class listarcategorias(ListView):
    template_name = 'appcategorias/listarcategorias.html'
    queryset = categorias.objects.all()

    def get_context_data(self,**kwargs):#permite pasar el contexto al template
        context = super().get_context_data(**kwargs)
        context['listarcategorias'] = context['categorias_list']
        context['contador'] = 0

        return context

class mostrarcategorias(DetailView):
     model=categorias
     template_name = 'appcategorias/editarcategorias.html'

     def get_context_data(self,**kwargs):#permite pasar el contexto al template
        context = super().get_context_data(**kwargs)
        context['micategoria'] = context['categorias']
        

        return context

def eliminarcategorias(request,id):
     consulta = categorias.objects.get(id = id)
     consulta.delete()
     return redirect('listarcategorias')

     




