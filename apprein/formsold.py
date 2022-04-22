

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from appblog.models import blogm
from appcategorias.models import categorias
from appforo.models import forom,categoria_forom
from apprein.models import perfil
from comentariosblog.models import comentariosblogm
from appeventos.models import eventosm

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
    titulo = forms.CharField(required=True,label='Titulo de la Entrada:',widget=forms.TextInput(attrs={'class':'form-control border-dark my-2','name':'titulof'}))
    contenido=forms.CharField(required=True,label='Descripción de la entrada:',widget=forms.Textarea(attrs={'class':'form-control border border-dark my-2','rows':2,'style':'min-height: 300px;','name':'contenidof'}))
    categoria=forms.CharField(label='Categoria:',widget=forms.TextInput(attrs={'class':'form-control border-dark my-2','name':'categoriaf'}))
    imagen =forms.ImageField(required=True,label='Ingrese una imagen',widget=forms.FileInput(attrs={'class':'form-control my-2','name':'imagenf'}))

    class Meta:
        model =forom
        fields=['titulo','contenido','categoria','imagen']


class actualizarperfilform(forms.ModelForm):
    biografia = forms.CharField(required=True,label='Biografía:',widget=forms.TextInput(attrs={'class':'form-control rounded-pill fs-5 fw-bolder mb-3','name':'biografiaperfil'}))
    imagenperfil =forms.ImageField(required=True,label='Ingrese una imagen',widget=forms.FileInput(attrs={'class':'form-control rounded-pill fs-5 fw-bolder mb-3','name':'imagenperfil'}))

    class Meta:
        model = perfil
        fields = ['biografia','imagenperfil']

class comentariosform(forms.ModelForm):
    titulocomentario = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control border-dark my-2'}))
    comentario = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control border-dark my-2'}))

    class Meta:
        model = comentariosblogm
        fields = ['titulocomentario','comentario']

class registrareventosform(forms.ModelForm):
    
    class Meta:
        model = eventosm
        fields = '__all__'