from django.views.generic import TemplateView
from django.shortcuts import render
from pesquisa.forms import FormPesquisaLocal 
from local.models import Local

#class HermesResultPage(TemplateView):
#    template_name = 'pesquisa/resultados.html'

def resultados_pesquisa(request):
    contexto = {}
    if request.GET.get('query',False):
        termo_de_busca = request.GET['query'].lower()
        lista_de_locais = Local.objects.filter(nome__icontains = termo_de_busca)
        contexto = {'lista_de_locais':lista_de_locais}
    return render(request,'pesquisa/resultados.html',contexto)
