from django.urls import path
from pesquisa.views import resultados_pesquisa
#from pesquisa.views import HermesResultPage

urlpatterns = [
    path('', resultados_pesquisa, name="pesquisa"),
]
