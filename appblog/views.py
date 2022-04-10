from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from appblog.models import blogm, categorias #importamos los modelos de la appblog
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login,logout
from apprein.forms import comentariosform
from comentariosblog.models import comentariosblogm
# from django.http import HttpResponseRedirect
# Create your views here.
# from proyecto_rein.forms import Inputimagen


def blog(request):
    
    blogs=blogm.objects.all()#importa todas las entradas de blog
    categoria=categorias.objects.all()
    cat = categorias.objects.all()



    return render(request,"appblog/blog.html",{
         'blogs':blogs,
         'categorias':categoria,
         'miscategorias':cat
    })
    
       

def registrarnuevaentrada(request):

     # sesionusuario = request.session.get('usuario')
     # print(sesionusuario)
     
     if request.method == 'POST':
          tituloe = request.POST['tituloe']
          contenidoe = request.POST['contenidoe']
          categoriae = request.POST['categoriae']
          imagene = request.FILES['imagene']
          # usuarioe = request.POST['usuarioe']
          # print(usuarioe)
          

          #usuario = User.objects.filter(username = request.session['usuario'])
          category=categorias.objects.filter(nombre=categoriae).exists()
          if category:
               #id_usuario = User.objects.get(username=request.session['usuario'])               
               catg = categorias.objects.get(nombre=categoriae)
               catg.nombre=categoriae
               catg.save()
               # usr = User.objects.get(username=usuarioe)
               # blogm.autor_id=usr.id
               # blogm.save()
               usuario = get_object_or_404(User,pk=request.user.id)
               documento = blogm(titulo=tituloe,descripcion=contenidoe,imagen=imagene,autor_id=usuario.id,categoria=catg)
               documento.save()
               
               
               if documento:
                    messages.success(request,'Información Guardada')
                    return redirect('blog')
          else:
               #id_usuario = User.objects.get(username=request.session['usuario']) 
               cat = categorias.objects.create(nombre=categoriae)
               cat.save()
               #HACER CONSU   LTA MEDIANTE EL MODELO USER
               usuario = get_object_or_404(User,pk=request.user.id)
               documento = blogm.objects.create(titulo=tituloe,descripcion=contenidoe,imagen=imagene,autor_id=usuario.id,categoria=cat)
               documento.save()

               if documento:
                    messages.success(request,'Información Guardada')
                    return redirect('blog')
          

     return render(request,'appblog/nuevaentrada.html',{
          'miscategorias':categorias.objects.all()
     })    
   

def modificarentradablog(request,id):

    articuloblog = blogm.objects.get(id=id)
    categoria=categorias.objects.all()

    if request.method == 'POST':
          idarticuloe = request.POST['idarticulo']
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

               articulo = blogm.objects.filter(id=idarticuloe).exists()
               if articulo:
                    documento = blogm.objects.get(id=idarticuloe)
                    documento.titulo = tituloe
                    documento.descripcion = contenidoe
                    documento.imagen =imagene
                    documento.categoria=catg
                    documento.save()
                    messages.success(request,'Información Guardada')
                    return redirect('blog')

               

    return render(request,'appblog/modificarblog.html',{
          'articuloblog': articuloblog,
          'categoria':categoria,
          'miscategorias':categoria

     })


     

def vistaarticulocompleto(request,id):
     articulo = blogm.objects.get(id=id)
     com = comentariosblogm.objects.all()

     comentarioform = comentariosform()
     cat = categorias.objects.all()
     

     
     return render(request,'appblog/articuloblog.html',{

          'articulo':articulo,
          'formcomentarios':comentarioform,
          'comentarios':com,
          'miscategorias':cat

     })

def eliminararticulo(request, id):

     articulo = blogm.objects.get(id=id)
     articulo.delete()
     return redirect ('blog')



class busquedaarticulos(ListView):
     
  

     template_name = 'appblog/busquedablog.html'

     def get_queryset(self):
          return blogm.objects.filter(titulo__icontains=self.query())
     
     def query(self):
          return self.request.GET.get('buscar') 
     
     def get_context_data(self, **kwargs):

          context= super().get_context_data(**kwargs)
          context['query'] = self.query()
          context['datosencontrados'] = context['object_list']
          context['cantidad'] = context['object_list'].count()
          context['miscategorias'] = categorias.objects.all()


          return context

def guardarcomentario(request):

     if request.method == 'POST':
          idarticulo = request.POST['idarticulo']
          titulocomentario = request.POST['titulocomentario']
          textocomentario = request.POST['comentario']
          idusuario = request.POST['idusuario']

          idart = blogm.objects.get(id = idarticulo)
          iduser = User.objects.get(id=idusuario)
          if idart and iduser:
               nuevocomentario = comentariosblogm.objects.create(titulocomentario=titulocomentario,comentario=textocomentario,entradablogs_id=idart.id,autorcoment_id=iduser.id)
               if nuevocomentario:

                    nuevocomentario.save()
                    messages.success(request,'Comentario Publicado')
                    return redirect('blog')
               else:
                    messages.error(request,'Error al publicar comentario')



     return render(request,'appblog/articuloblog.html')

























# def registrarcomentario(request):
#      comentarioform = comentariosform()
#      contexto ={'formcomentario':comentarioform}
#      return render(request,'appblog/articuloblog.html',contexto)




        # art = request.GET['buscar']

     # if request.method == 'GET':   
     #      datos = request.GET['buscar']

     #      if datos:
     #           articuloblog = blogm.objects.filter(titulo__icontains=datos)
     #      elif datos=='':
     #           messages.error(request,'El campo de busqueda esta vacio')
     #      else:
     #           messages.error(request,'No hay resultados con ese criterio')
     # else:
     #       messages.error(request,'Peticion incorrecta')






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