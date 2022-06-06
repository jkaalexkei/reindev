from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from appblog.models import blogm
from appcategorias.models import categorias #importamos los modelos de la appblog
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login,logout
from reindev.forms import formblognuevo,actualizarblogsform
from appcomentarios.models import comentariosblogm
# from django.http import HttpResponseRedirect
# Create your views here.
# from proyecto_rein.forms import Inputimagen

def blog(request):
    blogs = blogm.objects.all()
    
    comentariosblog = comentariosblogm.objects.all()
    

    contexto = {'blogs':blogs,'comentariosblog':comentariosblog}

    return render(request,'appblog/blog.html',contexto)



def crearblog(request):
    usuario = get_object_or_404(User,pk=request.user.pk)
    
    if request.method == 'POST':
        # categoria = request.POST['categoriablog']
        # cat = categorias.objects.get(id=categoria)
        categoria = request.POST['categoriablog']
        formblog = formblognuevo(request.POST,request.FILES)
        if formblog.is_valid():
            blog = formblog.save(commit=False)
            blog.autorblog = usuario            
            blog.save()
            blog.categoriablog.add(categoria)
            # blog.save()
            print(categoria)
            messages.success(request,'Blog creado con éxito')
            
            return redirect('blog')
    else:
        formblog = formblognuevo()
    
    contexto = {'formblognuevo':formblog}

    return render(request,'appblog/nuevaentrada.html',contexto)

def editarblog(request,id):

    b = blogm.objects.get(id=id)
    blog = get_object_or_404(blogm,id=id)

    datos = {
        'blog':b,
        'formblog':actualizarblogsform(instance=blog)
    }

    if request.method == 'POST':
        formulario = actualizarblogsform(data=request.POST,instance=blog,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Información del blog Actualizada')
            return redirect('blog')
    else:
        formulario = actualizarblogsform()


    return render(request,'appblog/modificarblog.html',datos)

def eliminarblog(request,id):
    blog = blogm.objects.get(id=id)
    blog.delete()
    messages.success(request,'Blog Eliminado con éxito')
    return redirect ('blog')


class mostrarblog(DetailView):

    
    
    model = blogm

    template_name = 'appblog/articuloblog.html'
    
    #  def get_queryset(self):
    #       return blogm.objects.filter(titulo__icontains=self.query())
     
    #  def query(self):
    #       return self.request.GET.get('buscar') 
     
    def get_context_data(self, **kwargs):

        context= super().get_context_data(**kwargs)
        # print(context)
        context['datosencontrados'] = context['blogm']
        context['comentario'] = comentariosblogm.objects.all()
       
        return context


class busquedablog(ListView):
     
     template_name = 'appblog/busquedablog.html'

     def get_queryset(self):
          return blogm.objects.filter(tituloblog__icontains=self.query())
     
     def query(self):
          return self.request.GET.get('buscar') 
     
     def get_context_data(self, **kwargs):

          context= super().get_context_data(**kwargs)
          context['query'] = self.query()
          context['datosencontrados'] = context['blogm_list']
          context['cantidad'] = context['blogm_list'].count()
        #   context['miscategorias'] = categorias.objects.all()
          
        #   print(context)

          return context