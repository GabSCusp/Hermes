from django.shortcuts import render
from produtos.models import List

def home_view(request):
    listas_disponiveis = List.objects.all()
    return render(request, 'home/home.html', {'listas_disponiveis': listas_disponiveis})
