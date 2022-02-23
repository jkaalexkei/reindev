
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




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


    
     