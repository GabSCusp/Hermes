from django.shortcuts import redirect, render
from produtos.models import List

def home_view(request):
    if request.user.is_authenticated:
        listas_disponiveis = List.objects.all()
        return render(request, 'home/home.html', {'listas_disponiveis': listas_disponiveis})
    return redirect('login')
