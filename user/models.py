from django.contrib.auth.models import User
from django.db import models
from local.models import Local
from django.contrib.auth.forms import UserCreationForm

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favoritos = models.ManyToManyField(Local)

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','email']
