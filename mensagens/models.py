from django.db import models 

class MensagemParaSuporte(models.Model):
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()

    def __str__(self):
        return self.assunto
