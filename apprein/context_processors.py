from .constant import categorias


def data_templates(request):
    return{
        'categorias':categorias
    }