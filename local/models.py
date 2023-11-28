from django.db import models

class Local(models.Model):
    latitude = models.FloatField(null=True,default=None,verbose_name="latitude do local")
    longitude = models.FloatField(null=True,default=None,verbose_name="longitude do local")
    status = models.BooleanField(null=True, default=False)
