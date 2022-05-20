
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from appblog.models import blogm
from appeventos.models import eventosm

from reindev.forms import comentariosblogform,comentarioseventoform
from . models import comentariosblogm,comentarioseventosm
# Create your views here.


def agregarcomentarioblog(request,id):
    blog = get_object_or_404(blogm,id=id)
    if request.method=='POST':
        formcomentario = comentariosblogform(request.POST)
        if formcomentario.is_valid():
            comentario = formcomentario.save(commit=False)
            comentario.autorcomentario = request.user
            comentario.comentariosblog = blog
            comentario.save()
            return redirect ('blog')
    else:
        formcomentario = comentariosblogform()

    contexto = {'formcomentario':formcomentario, 'blog':blog}

    return render(request,'appcomentarios/agregarcomentariosblog.html',contexto)

def agregarcomentarioeventos(request,id):
    evento = get_object_or_404(eventosm,id=id)
    if request.method=='POST':
        formcomentarioevento = comentarioseventoform(request.POST)
        if formcomentarioevento.is_valid():
            comentario = formcomentarioevento.save(commit=False)
            comentario.autorcomentarioeventos = request.user
            comentario.comentariosevento = evento
            comentario.save()
            return redirect ('eventos')
    else:
        formcomentario = comentarioseventoform()

    contexto = {'formcomentario':formcomentario, 'evento':evento}

    return render(request,'appcomentarios/agregarcomentarioseventos.html',contexto)

# def actualizarcategorias(request):
#      if request.method == 'POST':
#           idcategoria =request.POST['idcategoria']
#           nombrecategoria = request.POST['nombrecategoria']
#           bcategoria = categorias.objects.filter(id = idcategoria).exists()
#           if bcategoria:
#                cat = categorias.objects.get(id = idcategoria)
#                cat.nombre = nombrecategoria
#                cat.save()
#                messages.success(request,'Categoria Actualizada')
#                return redirect('listarcategorias')
               
#           # else:
#           #      nuevacategoria = categorias.objects.create(nombre=nombrecategoria)
#           #      if nuevacategoria:
#           #           nuevacategoria.save()
#           #           messages.success(request,'Categoria creada satisfactoriamente')
#           #           return redirect('home')
#           #      else:
#           #           messages.error(request,'error')
#      return render(request,'appcategorias/listarcategorias.html',{})

# def crearcategorias(request):
    
#      if request.method == 'POST':
#           nombrecategoria = request.POST['nombrecategoria']
#           buscarcategoria = categorias.objects.filter(nombre = nombrecategoria).exists()
#           if buscarcategoria:
#                cat = categorias.objects.get(nombre = nombrecategoria)
#                # cat.nombre = nombrecategoria
#                # cat.save()
#                messages.warning(request,'Categoria ya existe')
#                return redirect('listarcategorias')
               
#           else:
#                nuevacategoria = categorias.objects.create(nombre=nombrecategoria)
#                if nuevacategoria:
#                     nuevacategoria.save()
#                     messages.success(request,'Categoria creada satisfactoriamente')
#                     return redirect('listarcategorias')
#                else:
#                     messages.error(request,'error')

#      return render(request,'appcategorias/categorias.html')



# class listarcategorias(ListView):
#     template_name = 'appcategorias/listarcategorias.html'
#     queryset = categorias.objects.all()

#     def get_context_data(self,**kwargs):#permite pasar el contexto al template
#         context = super().get_context_data(**kwargs)
#         context['listarcategorias'] = context['categorias_list']
#         context['contador'] = 0

#         return context

# class mostrarcategorias(DetailView):
#      model=categorias
#      template_name = 'appcategorias/editarcategorias.html'

#      def get_context_data(self,**kwargs):#permite pasar el contexto al template
#         context = super().get_context_data(**kwargs)
#         context['micategoria'] = context['categorias']
        

#         return context

# def eliminarcategorias(request,id):
#      consulta = categorias.objects.get(id = id)
#      consulta.delete()
#      return redirect('listarcategorias')



# def crearsubcategorias(request):
#      if request.method == 'POST':
#           formsubcategorias = registrarsubcategoriasform(request.POST)
#           if formsubcategorias.is_valid():
#                formsubcategorias.save()
#                messages.success(request,'Subcategoria Agregada con éxito')
#                return redirect ('listarcategorias')
#      else:
#           formsubcategorias = registrarsubcategoriasform()
     
#      return render(request,'appcategorias/registrarsubcategorias.html',{
#           'formsubcategorias':formsubcategorias
#      })


# def listarsubcategorias(request,id):
    
#      sub = subcategorias.objects.filter(categoriarel_id = id)
#      # subcat = subcategorias.objects.get(categoriarel_id = id)
     
#      contexto = {'listarsubcategorias':sub,}

#      # print(resultado)

#      return render(request,'appcategorias/listarsubcategorias.html',contexto)

