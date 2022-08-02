
from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from appeventos.models import eventosm
from appforo.models import forom
from reindev.forms import crearcuentaform, actualizarperfilform,registrareventosform
from .models import perfil
from appblog.models import blogm
# from appblog.models import categorias
from appcategorias.models import categorias
from django.core.paginator import Paginator
from django.http import Http404
from appblog.models import notificacionesblog
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from django.db.models import Q

# from appblog.models import blog #importamos los modelos de la appblog
# Create your views here.


def home(request):

     articulospublicados = blogm.objects.all()[:3]
     eventos = eventosm.objects.all()[:3]
     

     

     page = request.GET.get('page',1)

     try:
          paginator = Paginator(eventos,3)
          eventos = paginator.page(page)
     except:
          raise Http404     

     contexto = {
          'articulospublicados':articulospublicados,
          'eventos':eventos,
          'foros':forom.objects.all()[:3],
          'paginator':paginator,
                
          
     }

     return render(request,"apprein/home.html",contexto)


# def calendario(request):
#      categoriasb = categorias.objects.all()

#      contexto= {
#           # 'miscategorias':categoriasb
#      }

#      return render(request,"apprein/calendario.html",contexto)

def iniciarsesion(request):

     # if request.method=='POST':
     #      messages.success(request,f"{username} Te has logueado correctamente")

     if request.method == 'POST':
          usuario = request.POST.get('username')
          clave = request.POST.get('password')

          user = authenticate(username=usuario,password=clave)

          if user:
               login(request,user)
              
               nombreusuario=User.objects.all()

               for usr in nombreusuario:
                    if usr.username == usuario:
                         request.session['usuario'] = usr.username
                         messages.success(request,'Hola {}'.format(usr.first_name))
                         
                         return redirect ('home')
                         
                    
               
          else:
               messages.error(request,'Usuario o Clave Inválida')
               # print('usuario no autenticado')
          
     

     return render(request,"apprein/login.html")

def cerrarsesion(request):

     logout(request)
     messages.success(request,'Sesión Finalizada con exito')
     request.session['usuario'] = None
     print('sesion cerrada')
     return redirect('home')

def crearcuenta(request):
     
     if request.method == 'POST':
          form = crearcuentaform(request.POST)
          if form.is_valid():
               form.save()
               username=form.cleaned_data['username']
               messages.success(request,'Cuenta creada satisfactoriamente')
               return redirect('home')
     else:
          form = crearcuentaform()
     
     contexto = {'form':form}

     return render(request,'apprein/crearcuenta.html',contexto)

def perfil(request,usuario):
     us = User.objects.get(username = usuario )
     articulosbloguser = blogm.objects.filter(autorblog_id = us.id)
     articulosforouser = forom.objects.filter(autorforo_id=us.id)
     articuloseventouser = eventosm.objects.filter(autorevento_id=us.id)
     contexto ={
          'usuario':usuario, 
          'articulosblog':articulosbloguser,
          'articulosforo':articulosforouser,
          'articulosevento':articuloseventouser
          
          }
     
     return render(request,'apprein/perfil.html',contexto)

def editarperfil(request):

     if request.method == 'POST':
          formuser = crearcuentaform(request.POST, instance=request.user)
          formperfil = actualizarperfilform(request.POST, request.FILES, instance=request.user.perfil)

          if formuser.is_valid() and formperfil.is_valid():
               formuser.save()
               formperfil.save()
               return redirect('home')
     else:
          formuser = crearcuentaform(instance = request.user)
          formperfil = actualizarperfilform()
     
     contexto = {
          'formuser': formuser,
          'formperfil':formperfil,
          # 'miscategorias':categorias.objects.all()
     }

     return render(request,'apprein/editarperfil.html',contexto)

def eliminarperfil(request,usuario):
     usuario = User.objects.get(username = usuario)
     usuario.delete()

     return redirect('home')


def buscardorgeneral(request):
     valor = request.GET.get('buscar')
     articulosblog = blogm.objects.filter(tituloblog__icontains = valor).order_by('-created')
     articuloforo = forom.objects.filter(tituloforo__icontains = valor).order_by('-created')
     articuloevento = eventosm.objects.filter(tituloevento__icontains = valor).order_by('-created')

     contexto = {
          'articuloblog':articulosblog,
          'articuloforo':articuloforo,
          'articuloevento':articuloevento,
          'resultadosblog': blogm.objects.filter(tituloblog__icontains = valor).count(),
          'resultadosforo': forom.objects.filter(tituloforo__icontains = valor).count(),
          'resultadosevento': eventosm.objects.filter(tituloevento__icontains = valor).count(),
          'valor':valor,
          
          
     }
    
     return render(request,'apprein/buscadorglobal.html',contexto)

# def resultadosporcategoria(request):
#      return render(request,'apprein/resultadosporcategoria.html',{'mensaje':'hola mundo'})

def resultadosporcategoria(request,id):   
    
     articuloblog = blogm.objects.filter(categoriablog = id)
     
     articuloforo = forom.objects.filter(categoriasforo = id)
     articuloevento = eventosm.objects.filter(categoriaevento = id)
     valor = categorias.objects.get(id=id)
     contexto = {
          
          'articuloblog': articuloblog,
          'articuloforo': articuloforo,
          'articuloevento': articuloevento,
          'valor':valor,
          'resultadosblog': blogm.objects.filter(categoriablog = id).count(),
          'resultadosforo': forom.objects.filter(categoriasforo = id).count(),
          'resultadosevento': eventosm.objects.filter(categoriaevento = valor).count(),
     }

     return render(request,'apprein/resultadosporcategoria.html',contexto)


def listarusuarios(request):
     usuarios = User.objects.all()

     contexto = {
          'usuarios':usuarios
     }

     return render(request,'apprein/listadousuarios.html',contexto)











































# def actividad(request):
#      pass
#      return render(request,'apprein/actividad.html')

     # if request.method=='POST':
     #      formcategorias = crearcategoriasform(request.POST)
     #      if formcategorias.is_valid():
     #           formcategorias.save()
     #           messages.success(request,'Categoria creada satisfactoriamente')
     #           return redirect('home')
               
     # else:
     #      formcategorias = crearcategoriasform()

     
     # # contexto = { 'formcategorias':formcategorias}

     # return render(request,'apprein/home.html',
     # { 'formcategorias':formcategorias}
     # )



     
# def blog(request):

#     blogs=blog.objects.all()#importa todas las entradas de blog

#     return render(request,"appRein/blog.html",{'blogs':blogs})


# def foro(request):
#      return render(request,"appRein/foro.html")