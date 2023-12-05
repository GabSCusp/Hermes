from django.db import models
from django.conf import settings


class Produto(models.Model):
    name = models.CharField(max_length=255)
    preço = models.IntegerField()
    Local=models.CharField(max_length=255)
    poster_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name} ({self.preço}) {self.Local}'


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'


class List(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        return f'{self.name} by {self.author}'
    
