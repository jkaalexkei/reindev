from appcategorias.models import categorias



def data_templates(request):
    cat = categorias.objects.all()
    return{
        'categorias':cat
    }