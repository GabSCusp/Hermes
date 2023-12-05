from django.urls import path 
from mensagens.views import enviar_mensagem

urlpatterns = [
    path('fale-conosco/', enviar_mensagem, name = "fale-conosco")
]
