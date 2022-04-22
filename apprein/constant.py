from appcategorias.models import categorias
CATEGORIAS = categorias.objects.all().order_by('-id')

