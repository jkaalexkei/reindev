from django.shortcuts import render,get_object_or_404,redirect
from appforo.models import forom
from . models import mensajechatforom,respuestachatforom
from reindev.forms import formeditarmensajechatforom, formmensajechatforom,formrespuestachatforom,formeditarrespuestachatforom
from django.contrib import messages
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


def editarmensajechatforo(request,id):

    mensajechat = get_object_or_404(mensajechatforom,id=id)
    foro = get_object_or_404(forom,id=mensajechat.fororel_id)

    datos = {
        'mensajechat':mensajechat,
        'formmensajechatforo': formeditarmensajechatforom(instance=mensajechat)
    }

    if request.method == 'POST':
        formmensajechat = formeditarmensajechatforom(request.POST,instance=mensajechat)
        if formmensajechat.is_valid():
            msg = formmensajechat.save(commit=False)
            msg.autormensaje = request.user
            msg.fororel = foro
            msg.save()
            return redirect('chatforo',id=mensajechat.fororel_id)
            
    else:
        formmensajechat = formeditarmensajechatforom()


    return render(request,'appchatforo/editarmensajechat.html',datos)

def eliminarmensajechatforo(request,id):
    mensajechat = mensajechatforom.objects.get(id=id)
    foro = get_object_or_404(forom,id =mensajechat.fororel_id)
    mensajechat.delete()
    messages.success(request,'Mensaje Eliminado')
    return redirect('chatforo',id=mensajechat.fororel_id)


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


def editarrespuestachatforo(request,id):
    
    respuestachat = get_object_or_404(respuestachatforom,id=id)
    mensajechat = get_object_or_404(mensajechatforom,id=respuestachat.mensajerelforo_id)
    foroarticulo = forom.objects.get(id = mensajechat.fororel_id)

    datos = {
        'respuestachat':respuestachat,
        'formrespuestachatforo': formeditarrespuestachatforom(instance=respuestachat)
    }

    if request.method == 'POST':
        formrespuestachat = formeditarrespuestachatforom(request.POST,instance=respuestachat)
        if formrespuestachat.is_valid():
            msg = formrespuestachat.save(commit=False)
            msg.autorrespuesta = request.user
            msg.fororel = foroarticulo
            msg.save()
            return redirect('chatforo',id=mensajechat.fororel_id)
            
    else:
        formrespuestachat = formeditarrespuestachatforom()


    return render(request,'appchatforo/editarrespuestachat.html',datos)

def eliminarrespuestachatforo(request,id):
    mensajechat = mensajechatforom.objects.get(id=id)
    foro = get_object_or_404(forom,id =mensajechat.fororel_id)
    mensajechat.delete()
    messages.success(request,'Mensaje Eliminado')
    return redirect('chatforo',id=mensajechat.fororel_id)