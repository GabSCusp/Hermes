from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from user.models import RegistroForm
from django.contrib import messages

class LoginPageView(TemplateView):
     template_name = 'user/login.html'

def Registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect('')
        messages.error(request, 'O registro falhou, informação inválida')
    form = RegistroForm()
    return render(request,'user/registro.html',{'form':form})

