from django.contrib.auth.views import TemplateView
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth import login, logout
from django.views.generic.base import View
from user.forms import RegistroForm
from django.contrib import messages
from user.models import PerfilUsuario
from local.models import Local
from django.contrib.auth.mixins import LoginRequiredMixin

def Registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect('home')
        messages.error(request, 'O registro falhou, informação inválida')
    form = RegistroForm()
    return render(request,'user/registro.html',{'form':form})

class UserConfigView(LoginRequiredMixin, TemplateView):
    template_name = "user/config_page.html"
    login_url = 'login'

class HermesLogOut(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('login'))

def list_favoritos(request):
    if request.user.is_authenticated:
        perfil_usuario, created = PerfilUsuario.objects.get_or_create(user=request.user)
        favoritos = perfil_usuario.favoritos.all()
        return render(request, 'user/favoritos.html', {'favoritos':favoritos})
    return redirect('login')

def add_favoritos(request, id_local):
    if request.user.is_authenticated:
        perfil_usuario, created = PerfilUsuario.objects.get_or_create(user=request.user)
        local = get_object_or_404(Local, id=id_local)

        if local not in perfil_usuario.favoritos.all():
            perfil_usuario.favoritos.add(local)
            return redirect('perfil')
        return redirect('home')
    return redirect('login')
