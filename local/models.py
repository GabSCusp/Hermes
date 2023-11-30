from django.db import models

class Local(models.Model):
    nome = models.CharField(max_length=100,null=True,verbose_name='nome do local na base de dados')
    latitude = models.FloatField(null=True,default=None,verbose_name="latitude do local")
    longitude = models.FloatField(null=True,default=None,verbose_name="longitude do local")
    status = models.BooleanField(null=True, default=False)
