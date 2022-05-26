from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib import messages
 #importamos los modelos de la appblog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# from appblog.views import registrarnuevaentrada
from appforo.models import forom

from reindev.forms import regitroentradaforo,actualizarforoform
from appcategorias.models import categorias
from appcomentarios.models import comentariosforom

# Create your views here.

def foro(request):

    foropublicacion=forom.objects.all()
    

    return render(request,"appforo/foro.html",{
        'foro':foropublicacion,
       
        })

def agregarforo(request):
    if request.method == 'POST':
        formularioforo = regitroentradaforo(request.POST,request.FILES)
        if formularioforo.is_valid():
            formularioforo.save()
            return redirect('foro')
    else:
        formularioforo = regitroentradaforo()

    return render(request,'appforo/agregarforo.html',
    {'formularioforo':formularioforo})

def editarforo(request,id):
    
    f = forom.objects.get(id=id)
    foro = get_object_or_404(forom,id=id)

    datos = {
        'foro':f,
        'formforo':actualizarforoform(instance=foro)
    }

    if request.method == 'POST':
        formulario = actualizarforoform(data=request.POST,instance=foro,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Información del foro Actualizada')
            return redirect('foro')
    else:
        formulario = actualizarforoform()


    return render(request,'appforo/editarforo.html',datos)

class busquedaforo(ListView):
     
     template_name = 'appforo/busquedaforo.html'

     def get_queryset(self):
          return forom.objects.filter(tituloforo__icontains=self.query())
     
     def query(self):
          return self.request.GET.get('buscar') 
     
     def get_context_data(self, **kwargs):

          context= super().get_context_data(**kwargs)
          context['query'] = self.query()
          context['datosencontrados'] = context['forom_list']
          context['cantidad'] = context['forom_list'].count()   

          return context


def eliminarforo(request, id):
    
     articuloforo = forom.objects.get(id=id)
     articuloforo.delete()
     return redirect ('foro')

class mostrarforo(DetailView):

    model = forom

    template_name = 'appforo/descripcionforo.html'
    
    #  def get_queryset(self):
    #       return blogm.objects.filter(titulo__icontains=self.query())
     
    #  def query(self):
    #       return self.request.GET.get('buscar') 
     
    def get_context_data(self, **kwargs):

        context= super().get_context_data(**kwargs)
        # print(context)
        context['datosencontrados'] = context['forom']

        context['comentarioforo'] = comentariosforom.objects.all()
       
        return context




     
# def crearforo(request):
#     usr = get_object_or_404(User,pk=request.user.id)
#     # cat = get_object_or_404(categoria_forom,pk=request.categoria.id)

#     if request.method=='POST':
#         form = regitroentradaforo(data=request.POST,files=request.FILES)
#         catf = categoria_forom.objects.filter(nombre = request.POST['categoria']).exists()
#         if catf:
#             cat = categoria_forom.objects.get(nombre= request.POST['categoria'])
#             cat.nombre= request.POST['categoria']
#             cat.save()
            
#         else:
#             cat = categoria_forom.objects.create(nombre = request.POST['categoria'])
#             cat.save()

#         if form.is_valid():
#             nuevoforo = form.save(commit=False)
#             nuevoforo.autorf = usr
#             nuevoforo.categoriasforo_id = cat.id
          
#             nuevoforo.save()
#             messages.success(request,'Foro Creado')
#             return redirect ('foro')
#     else:
#         form=regitroentradaforo()
        
#     contexto = {'form':form,
#                 'miscategorias':categorias.objects.all()    
#                 }

#     return render(request,'appforo/crearforo.html',contexto)



# def modificarentradaforo(request,id):
    
#     articuloforo = forom.objects.get(id=id)
#     categoria=categoria_forom.objects.all()

#     if request.method == 'POST':
#           idarticulof = request.POST['idarticulof']
#           titulof = request.POST['titulof']
#           contenidof = request.POST['contenidof']
#           categoriaf = request.POST['categoriaf']
#           imagenf = request.FILES['imagenf']

#                #usuario = User.objects.filter(username = request.session['usuario'])
#           category=categoria_forom.objects.filter(nombre=categoriaf).exists()
#           if category:
#                     #id_usuario = User.objects.get(username=request.session['usuario'])               
#                catg = categoria_forom.objects.get(nombre=categoriaf)
#                catg.nombre=categoriaf
#                catg.save()

#                articulo = forom.objects.filter(id=idarticulof).exists()
#                if articulo:
#                     documento = forom.objects.get(id=idarticulof)
#                     documento.titulo = titulof
#                     documento.contenido = contenidof
#                     documento.imagen =imagenf
#                     documento.categoriasforo=catg
#                     documento.save()
#                     messages.success(request,'Información Actualizada')
#                     return redirect('foro')

               

#     return render(request,'appforo/modificarforo.html',{
#           'articuloforo': articuloforo,
#           'categoria':categoria

#      })