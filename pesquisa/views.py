from django.shortcuts import redirect, render
from local.models import Local

def resultados_pesquisa(request):
    if request.user.is_authenticated:
        contexto = {}
        if request.GET.get('query',False):
            termo_de_busca = request.GET['query'].lower()
            lista_de_locais = Local.objects.filter(nome__icontains = termo_de_busca)
            contexto = {'lista_de_locais':lista_de_locais}
        return render(request,'pesquisa/resultados.html',contexto)
    return redirect('login')
