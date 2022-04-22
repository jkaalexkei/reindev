from django.shortcuts import render
from django.views.generic.list import ListView
from .models import categorias
# Create your views here.


# def categorias(request):
#     categorias = categorias.objects.all()
#     contexto = {'categorias':categorias}
#     return render(request,'categorias/categorias.html',contexto)


# class listarcategorias(ListView):
#     template_name = 'categorias/categorias.html'
#     queryset = categorias.objects.all().order_by('-id')

#     def get_context_data(self,**kwargs):#permite pasar el contexto al template
#         context = super().get_context_data(**kwargs)
#         context['cat'] = context['categorias_list']

#         return context
