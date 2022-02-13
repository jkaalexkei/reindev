from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from django.contrib import messages
from appblog.models import blogm, categorias #importamos los modelos de la appblog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# from django.http import HttpResponseRedirect
# Create your views here.
# from proyecto_rein.forms import Inputimagen

def blog(request):
    
    blogs=blogm.objects.all()#importa todas las entradas de blog
    categoria=categorias.objects.all()

    return render(request,"appblog/blog.html",{
         'blogs':blogs,
         'categorias':categoria
    })
    
       

def registrarnuevaentrada(request):

     # sesionusuario = request.session.get('usuario')
     # print(sesionusuario)

     if request.method == 'POST':
          tituloe = request.POST['tituloe']
          contenidoe = request.POST['contenidoe']
          categoriae = request.POST['categoriae']
          imagene = request.FILES['imagene']

          #usuario = User.objects.filter(username = request.session['usuario'])
          category=categorias.objects.filter(nombre=categoriae).exists()
          if category:
               #id_usuario = User.objects.get(username=request.session['usuario'])               
               catg = categorias.objects.get(nombre=categoriae)
               catg.nombre=categoriae
               catg.save()
               documento = blogm.objects.create(titulo=tituloe,descripcion=contenidoe,imagen=imagene,categoria=catg)
               documento.save()
               if documento:
                    messages.success(request,'Información Guardada')
                    return redirect('blog')
          else:
               #id_usuario = User.objects.get(username=request.session['usuario']) 
               cat = categorias.objects.create(nombre=categoriae)
               cat.save()
               #HACER CONSULTA MEDIANTE EL MODELO USER

               documento = blogm.objects.create(titulo=tituloe,descripcion=contenidoe,imagen=imagene,categoria=cat)
               documento.save()

               if documento:
                    messages.success(request,'Información Guardada')
                    return redirect('blog')
          

     return render(request,'appblog/nuevaentrada.html',{})    
   

def modificarentradablog(request,id):

     identrada = id
     print(identrada)

     

     # if request.method == 'POST':
     #      tituloe = request.POST['tituloe']
     #      contenidoe = request.POST['contenidoe']
     #      categoriae = request.POST['categoriae']
     #      imagene = request.FILES['imagene']

     #      #usuario = User.objects.filter(username = request.session['usuario'])
     #      category=categorias.objects.filter(nombre=categoriae).exists()
     #      if category:
     #           #id_usuario = User.objects.get(username=request.session['usuario'])               
     #           catg = categorias.objects.get(nombre=categoriae)
     #           catg.nombre=categoriae
     #           catg.save()
     #           documento = blogm(titulo=tituloe,descripcion=contenidoe,imagen=imagene,categoria=catg)
     #           documento.save()
     #           if documento:
     #                messages.success(request,'Información Actualizada')
     #                return redirect('blog')
     #      # else:
          #      #id_usuario = User.objects.get(username=request.session['usuario']) 
          #      cat = categorias.objects.create(nombre=categoriae)
          #      cat.save()
          #      #HACER CONSULTA MEDIANTE EL MODELO USER

          #      documento = blogm.objects.create(titulo=tituloe,descripcion=contenidoe,imagen=imagene,categoria=cat)
          #      documento.save()

          #      if documento:
          #           messages.success(request,'Información Guardada')
          #           return redirect('blog')




     return render(request,'appblog/modificarblog.html',{
          

     })


     

def vistaarticulocompleto(request,id):
     articulo = blogm.objects.get(id=id)

     
     return render(request,'appblog/articuloblog.html',{

          'articulo':articulo

     })

def eliminararticulo(request, id):

     articulo = blogm.objects.get(id=id)

     articulo.delete()
     return redirect ('blog')



































#    if request.method == 'POST':
#           usuario = request.POST.get('username')
#           clave = request.POST.get('password')

#           user = authenticate(username=usuario,password=clave)

#           if user:
#                login(request,user)
#                nombreusuario=User.objects.all()

#                for usr in nombreusuario:
#                     if usr.username == usuario:
#                         print(usr.first_name)
    
     
        
        #  'registrarnuevaentrada': form_registrarnuevaentrada

     

    # form_registrarnuevaentrada = FormRegistrarEntrada(request.POST or None)

    # if request.method == 'POST' and form_registrarnuevaentrada.is_valid():

    #     tituloE=form_registrarnuevaentrada.cleaned_data.get('tituloEntrada')
    #     contenidoE=form_registrarnuevaentrada.cleaned_data.get('contenidoEntrada')
    #     # categoriaE=registrarnuevaentrada.cleaned_data.get('categoriasEntrada')
    #    # imagenE=form_registrarnuevaentrada.get('imagenDestacada')

    #     nuevo=blog.objects.create(titulo=tituloE,descripcion=contenidoE,imagen='autismo.jpg')

    #     if nuevo:
    #         nuevo.save()
    #         messages.success(request,'Entrada creada con exito')
    #         return redirect('blog')
    #     else:
    #         print('error al guardar la informacion')

  



    # return render(request,'appblog/nuevaentrada.html',{

    #     'registrarnuevaentrada': form_registrarnuevaentrada

    # })