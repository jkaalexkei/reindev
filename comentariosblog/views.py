# from django.shortcuts import render,get_object_or_404
# from django.shortcuts import redirect
# from django.contrib import messages
# from appblog.models import blogm, categorias #importamos los modelos de la appblog
# from django.contrib.auth.models import User
# from django.views.generic.list import ListView
# from django.contrib.auth import authenticate, login,logout
# from apprein.forms import comentariosform
# from comentariosblog.models import comentariosblogm
# from appblog.models import blogm

# Create your views here.


# def mostrarcomentarios(request):

#      comentarios = comentariosblogm.objects.all()

     
     
#      return render(request,'appblog/articuloblog.html',{
#          'comentarios':comentarios,
#      })


# def guardarcomentario(request):

     

#      if request.method == 'POST':
#           idarticulo = request.POST['idarticulo']
#           formcomentario = comentariosform(data=request.POST)

#           if (formcomentario.is_valid()):
#                formcomentario.save(commit=False)
#                artblog = blogm.objects.get(id=idarticulo)
#                entradablog = comentariosblogm()
#                entradablog.entradablog_id = artblog.id
#                entradablog.save()
#                formcomentario.save()
#                return redirect('articuloblog')
#      else:
#           formcomentario = comentariosform()

     
#      contexto = {'form':formcomentario}


#      return render(request,'appblog/articuloblog.html',contexto)

     