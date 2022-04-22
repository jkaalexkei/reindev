from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from django.contrib import messages
 #importamos los modelos de la appblog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# from appblog.views import registrarnuevaentrada
from appforo.models import forom
from appforo.models import categoria_forom
from reindev.forms import regitroentradaforo
from appcategorias.models import categorias

# Create your views here.

def foro(request):

    foropublicacion=forom.objects.all()
    categoriaforo=categoria_forom.objects.all()
    cat = categorias.objects.all()
    

    
    


    return render(request,"appforo/foro.html",{
        'foro':foropublicacion,
        'categoria':categoriaforo,
        # 'miscategorias':cat
        })


def crearforo(request):
    usr = get_object_or_404(User,pk=request.user.id)
    # cat = get_object_or_404(categoria_forom,pk=request.categoria.id)

    if request.method=='POST':
        form = regitroentradaforo(data=request.POST,files=request.FILES)
        catf = categoria_forom.objects.filter(nombre = request.POST['categoria']).exists()
        if catf:
            cat = categoria_forom.objects.get(nombre= request.POST['categoria'])
            cat.nombre= request.POST['categoria']
            cat.save()
            
        else:
            cat = categoria_forom.objects.create(nombre = request.POST['categoria'])
            cat.save()

        if form.is_valid():
            nuevoforo = form.save(commit=False)
            nuevoforo.autorf = usr
            nuevoforo.categoriasforo_id = cat.id
          
            nuevoforo.save()
            messages.success(request,'Foro Creado')
            return redirect ('foro')
    else:
        form=regitroentradaforo()
        
    contexto = {'form':form,
                'miscategorias':categorias.objects.all()    
                }

    return render(request,'appforo/crearforo.html',contexto)



def modificarentradaforo(request,id):
    
    articuloforo = forom.objects.get(id=id)
    categoria=categoria_forom.objects.all()

    if request.method == 'POST':
          idarticulof = request.POST['idarticulof']
          titulof = request.POST['titulof']
          contenidof = request.POST['contenidof']
          categoriaf = request.POST['categoriaf']
          imagenf = request.FILES['imagenf']

               #usuario = User.objects.filter(username = request.session['usuario'])
          category=categoria_forom.objects.filter(nombre=categoriaf).exists()
          if category:
                    #id_usuario = User.objects.get(username=request.session['usuario'])               
               catg = categoria_forom.objects.get(nombre=categoriaf)
               catg.nombre=categoriaf
               catg.save()

               articulo = forom.objects.filter(id=idarticulof).exists()
               if articulo:
                    documento = forom.objects.get(id=idarticulof)
                    documento.titulo = titulof
                    documento.contenido = contenidof
                    documento.imagen =imagenf
                    documento.categoriasforo=catg
                    documento.save()
                    messages.success(request,'Información Actualizada')
                    return redirect('foro')

               

    return render(request,'appforo/modificarforo.html',{
          'articuloforo': articuloforo,
          'categoria':categoria

     })


def eliminarforo(request, id):
    
     articuloforo = forom.objects.get(id=id)
     articuloforo.delete()
     return redirect ('foro')