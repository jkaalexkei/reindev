from appcategorias.models import categorias, subcategorias
from appblog.models import blogm, notificacionesblog
from appforo.models import forom,notificacionesforo
from appeventos.models import eventosm,notificacioneseventos



def data_templates(request):
    cat = categorias.objects.all()
    subcat = subcategorias.objects.all()
    blog = blogm.objects.all() 
    notiblog = notificacionesblog.objects.all().count()
    notiforo = notificacionesforo.objects.all().count()
    notieventos = notificacioneseventos.objects.all().count()

    return{
        'categorias':cat,
        'subcat':subcat,
        'notificaciones':(notiblog+notiforo+notieventos)
    }