from django.contrib.auth.models import User
from django.db import models
from local.models import Local

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favoritos = models.ManyToManyField(Local)
