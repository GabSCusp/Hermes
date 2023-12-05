from django.db import models

class Local(models.Model):
    nome = models.CharField(max_length=100,null=True,blank=False ,verbose_name='nome do local na base de dados')
    latitude = models.FloatField(null=True, blank=True, verbose_name="latitude do local")
    longitude = models.FloatField(null=True, blank=True, verbose_name="longitude do local")
    status = models.BooleanField(null=False, default=False)
    CEP = models.CharField(null=True, blank=True, max_length=100, name="CEP")
    endereço = models.CharField(null=True, blank=False, max_length=250, name = 'endereço')
    descrição = models.CharField(null=True,max_length=500, name="descrição")
    imagem = models.ImageField(upload_to='local/imagens_de_locais',null=True, blank=False, name="imagem")
