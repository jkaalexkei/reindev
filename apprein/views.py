
from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from appeventos.models import eventosm
from reindev.forms import crearcuentaform, actualizarperfilform,registrareventosform
from .models import perfil
from appblog.models import blogm
# from appblog.models import categorias
from appcategorias.models import categorias


# from appblog.models import blog #importamos los modelos de la appblog
# Create your views here.


def home(request):

     articulospublicados = blogm.objects.all()
     eventos = eventosm.objects.all().order_by('created')     

     contexto = {
          'articulospublicados':articulospublicados,
          'eventos':eventos          
   
          
     }

     return render(request,"apprein/home.html",contexto)


def calendario(request):
     categoriasb = categorias.objects.all()

     contexto= {
          # 'miscategorias':categoriasb
     }

     return render(request,"apprein/calendario.html",contexto)

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
     usuario = User.objects.get(username = usuario )
     articulosbloguser = usuario.blogms.all()
     articulosforouser = usuario.foroms.all()
     articuloseventouser = usuario.eventosm.all()
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