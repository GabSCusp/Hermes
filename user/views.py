from django.contrib.auth.views import TemplateView
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout
from django.views.generic.base import View
from user.forms import RegistroForm
from django.contrib import messages

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

class UserConfigView(TemplateView):
    template_name = "user/config_page.html"

class HermesLogOut(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('login'))
