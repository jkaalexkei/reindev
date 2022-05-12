from appcategorias.models import categorias, subcategorias



def data_templates(request):
    cat = categorias.objects.all()
    subcat = subcategorias.objects.all()
    return{
        'categorias':cat,
        'subcat':subcat
    }