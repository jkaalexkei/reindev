

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from appblog.models import blogm
from appeventos.models import eventosm
from appforo.models import forom
from appcomentarios.models import comentariosblogm, comentariosforom,comentarioseventosm

from reindev.forms import comentariosblogform,comentarioseventoform,comentariosforoform,editarcomentariosforoform
from . models import comentariosblogm,comentarioseventosm,comentariosforom
# Create your views here.

# def comentariosblog(request):
#     coment_blog = comentariosblogm.objects.all()

#     contexto = {
#         'comentariosblog':coment_blog
#     }

#     return render('appcoment')


def agregarcomentarioblog(request,id):
    blog = get_object_or_404(blogm,id=id)
    if request.method=='POST':
        formcomentario = comentariosblogform(request.POST)
        if formcomentario.is_valid():
            comentario = formcomentario.save(commit=False)
            comentario.autorcomentario = request.user
            comentario.comentariosblog = blog
            comentario.save()
            return redirect ('mostrarblog',pk=blog.id)
    else:
        formcomentario = comentariosblogform()

    contexto = {'formcomentario':formcomentario, 'blog':blog}

    return render(request,'appcomentarios/agregarcomentariosblog.html',contexto)

def editarcomentarioforo(request,id):
    
    f = comentariosforom.objects.get(id=id)
    comentarioforo = get_object_or_404(comentariosforom,id=id)
    foro = get_object_or_404(forom,id=comentarioforo.comentariosfororel_id)


    datos = {
        'comentarioforo':f,
        'formcomentarioforo':editarcomentariosforoform(instance=comentarioforo)
       
    }

    if request.method == 'POST':
        formulario = editarcomentariosforoform(data=request.POST,instance=comentarioforo)
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.autorcomentario = request.user
            comentario.comentariosfororel = foro
            comentario.save()
            # messages.success(request,'Información del blog Actualizada')
            return redirect ('mostrarforo',pk=comentarioforo.comentariosfororel_id)
    else:
        formulario = editarcomentariosforoform()


    return render(request,'appcomentarios/editarcomentariosforo.html',datos)


def eliminarcomentarioforo(request,id):
    comentarioforo = comentariosforom.objects.get(id=id)
    comentarioforo.delete()
    # messages.success(request,'Blog Eliminado con éxito')
    return redirect ('mostrarforo',pk=comentarioforo.comentariosfororel_id)

def agregarcomentarioeventos(request,id):
    evento = get_object_or_404(eventosm,id=id)
    if request.method=='POST':
        formcomentarioevento = comentarioseventoform(request.POST)
        if formcomentarioevento.is_valid():
            comentario = formcomentarioevento.save(commit=False)
            comentario.autorcomentarioeventos = request.user
            comentario.comentariosevento = evento
            comentario.save()
            return redirect ('mostrarevento',pk=evento.id)
    else:
        formcomentario = comentarioseventoform()

    contexto = {'formcomentario':formcomentario, 'evento':evento}

    return render(request,'appcomentarios/agregarcomentarioseventos.html',contexto)

def agregarcomentarioforo(request,id):
    foroart = get_object_or_404(forom,id=id)
    
    f = forom.objects.get(id = id)
    print(f.id)
    if request.method=='POST':
        
        formcomentarioforo = comentariosforoform(request.POST)
        # print(formcomentarioforo)
        if formcomentarioforo.is_valid():
            comentario = formcomentarioforo.save(commit=False)
            comentario.autorcomentarioforo = request.user
            comentario.comentariosfororel = foroart
            comentario.save()
            return redirect ('mostrarforo',pk=foroart.id)
    else:
        formcomentarioforo = comentariosforoform()

    contexto = {'formcomentarioforo':formcomentarioforo, 'foroart':foroart}

    return render(request,'appcomentarios/agregarcomentariosforo.html',contexto)









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


