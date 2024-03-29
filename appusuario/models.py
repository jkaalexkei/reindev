from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class usuariosmManager(BaseUserManager):
    def create_user(self,email,username,password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')

        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
            # nombres = nombres,
            # apellidos = apellidos
        )

        usuario.set_password(password)
        usuario.save()
        return usuario


    def create_superuser(self,username,email,password):
        usuario = self.create_user(        
            email,
            username = username,       
            # nombres = nombres,
            # apellidos = apellidos,
            password = password
            
        )

        usuario.usuario_administrador = True
        usuario.save()
        return usuario

class usuariosm(AbstractBaseUser):
    username = models.CharField('Usuario', unique=True,max_length=100)
    email = models.EmailField('Correo',max_length=254,unique=True,null=False)
    nombres = models.CharField('Nombres',max_length=200,blank=True,null=True)
    apellidos =models.CharField('Apellidos',max_length = 200,blank=True,null=True)
    usuario_activo =models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=True)
    objects = usuariosmManager()
 
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS= ['email']

    def __str__(self):
        return f'{self.username}'
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador