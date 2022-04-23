from appcategorias.models import categorias
categorias = categorias.objects.all().order_by('nombre')

