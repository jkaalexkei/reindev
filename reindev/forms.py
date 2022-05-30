from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from requests import request

from appblog.models import blogm
from appcategorias.models import categorias, subcategorias
from appforo.models import forom
from apprein.models import perfil
from appcomentarios.models import comentariosblogm, comentarioseventosm,comentariosforom
from appeventos.models import eventosm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from appchatforo.models import mensajechatforom,respuestachatforom

class crearcategoriasform(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-pill fs-5 fw-bolder mb-3','placeholder':'Ingrese Nombre de la Categoria'}))
    class Meta:
        model=categorias
        fields=['nombre']


class crearcuentaform(UserCreationForm):
    first_name=forms.CharField(label='Nombre:',widget=forms.TextInput(attrs={'class':'form-control rounded-pill fs-5 fw-bolder mb-3','placeholder':'Ingrese un nombre'}))
    last_name=forms.CharField(label='Apellido: ',widget=forms.TextInput(attrs={'class':'form-control rounded-pill fs-5 fw-bolder mb-3','placeholder':'Ingrese un apellido'}))
    email = forms.EmailField(label='Email: ',widget=forms.EmailInput(attrs={'class':'form-control rounded-pill fs-5 fw-bolder mb-3','placeholder':'Ingrese un email'}))
    username=forms.CharField(label='Usuario: ',widget=forms.TextInput(attrs={'class':'form-control rounded-pill fs-5 fw-bolder mb-3','placeholder':'Ingrese un Usuario'}))
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control rounded-pill fs-5 fw-bolder mb-3','placeholder':'Ingrese una Contraseña'}))
    password2 = forms.CharField(label='Confirme Password',widget=forms.PasswordInput(attrs={'class':'form-control rounded-pill fs-5 fw-bolder mb-3','placeholder':'Confirme la contraseña'}))

    class Meta:
        model= User
        fields=['first_name','last_name','username','email','password1','password2']
        help_texts = {k:'' for k in fields}

class regitroentradaforo(forms.ModelForm):

   class Meta:
        model =forom
        fields=['tituloforo','contenidoforo','imagenforo','categoriasforo']

class actualizarforoform(forms.ModelForm):
    class Meta:
        model = forom
        fields = '__all__'


class actualizarperfilform(forms.ModelForm):
    biografia = forms.CharField(required=True,label='Biografía:',widget=forms.TextInput(attrs={'class':'form-control rounded-pill fs-5 fw-bolder mb-3','name':'biografiaperfil'}))
    imagenperfil =forms.ImageField(required=True,label='Ingrese una imagen',widget=forms.FileInput(attrs={'class':'form-control rounded-pill fs-5 fw-bolder mb-3','name':'imagenperfil'}))

    class Meta:
        model = perfil
        fields = ['biografia','imagenperfil']

class comentariosblogform(forms.ModelForm):
    
    comentario = forms.CharField(label="Comentario",widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))

    class Meta:
        model = comentariosblogm
        fields = ['comentario']

class comentariosforoform(forms.ModelForm):
    
    comentarioforo = forms.CharField(label="Comentario",widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))

    class Meta:
        model = comentariosforom
        fields = ['comentarioforo']

class comentarioseventoform(forms.ModelForm):
    
    comentarioevento = forms.CharField(label='Comentario',widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))

    class Meta:
        model = comentarioseventosm
        fields = ['comentarioevento']

class registrareventosform(forms.ModelForm):
    
    
    class Meta:
        model = eventosm
        fields = ['tituloevento','contenidoevento','imagenevento','categoriaevento','eventolink','fechaevento','horaevento','tipodeevento','videoevento']

class actualizareventosform(forms.ModelForm):
       
    
    class Meta:
        model = eventosm
        fields = '__all__'


class registrarsubcategoriasform(forms.ModelForm):

    class Meta:
        model = subcategorias
        fields = '__all__'

class formblognuevo(forms.ModelForm):
    
    

    class Meta:
        model = blogm
        fields = ['tituloblog','contenidoblog','imagenblog','categoriablog']

class actualizarblogsform(forms.ModelForm):
    
    class Meta:
        model = blogm
        fields = ['tituloblog','contenidoblog','imagenblog','categoriablog']


class formmensajechatforom(forms.ModelForm):
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))
    class Meta:
        model=mensajechatforom
        fields = ['mensaje']


class formrespuestachatforom(forms.ModelForm):
    respuesta = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))
    class Meta:
        model=respuestachatforom
        fields = ['respuesta']