from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# from appblog.models import blog #importamos los modelos de la appblog
# Create your views here.

def home(request):

    return render(request,"apprein/home.html")

# def blog(request):

#     blogs=blog.objects.all()#importa todas las entradas de blog

#     return render(request,"appRein/blog.html",{'blogs':blogs})


# def foro(request):
#      return render(request,"appRein/foro.html")

def calendario(request):
     return render(request,"apprein/calendario.html")

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
               print('usuario no autenticado')
          
     

     return render(request,"apprein/login.html")

def cerrarsesion(request):

     logout(request)
     messages.success(request,'Sesión Finalizada con exito')
     request.session['usuario'] = None
     print('sesion cerrada')
     return redirect('home')
