from django.shortcuts import render,get_object_or_404,redirect
from appforo.models import forom
from . models import mensajechatforom,respuestachatforom
from reindev.forms import formmensajechatforom,formrespuestachatforom

# Create your views here.

def chatforo(request,id):
    forotema = get_object_or_404(forom,id=id)
    mensajes = mensajechatforom.objects.all()
    respuestas = respuestachatforom.objects.all()
    contexto = {'forotema':forotema,'mensajes':mensajes,'respuestas':respuestas}
    return render(request,'appchatforo/chatforo.html',contexto)


def guardarmensajechatforo(request,id):

    foroarticulo = get_object_or_404(forom,id=id)

    if request.method == 'POST':
        formmensaje = formmensajechatforom(request.POST)
        if formmensaje.is_valid():
            msg = formmensaje.save(commit=False)
            msg.autormensaje = request.user
            msg.fororel = foroarticulo
            msg.save()
            return redirect('chatforo',id=foroarticulo.id)
            
    else:
        formmensaje = formmensajechatforom()
    

    contexto = {'formmensaje':formmensaje,'foroarticulo':foroarticulo}

    return render(request,'appchatforo/agregarmensaje.html',contexto)

def guardarrespuestachatforo(request,id):
    
    # foroarticulo = get_object_or_404(forom,id=id)
    mensaje = get_object_or_404(mensajechatforom, id=id)
    foroarticulo = forom.objects.get(id = mensaje.fororel_id)

    if request.method == 'POST':
        formrespuesta = formrespuestachatforom(request.POST)
        if formrespuesta.is_valid():
            msg = formrespuesta.save(commit=False)
            msg.autorrespuesta = request.user
            msg.mensajerelforo = mensaje
            msg.save()
            return redirect('chatforo',id=foroarticulo.id)
            
    else:
        formrespuesta = formrespuestachatforom()
    

    contexto = {'formrespuesta':formrespuesta,'foroarticulo':foroarticulo,'mensajes':mensaje}

    return render(request,'appchatforo/agregarrespuesta.html',contexto)