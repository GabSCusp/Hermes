from django.shortcuts import render, redirect
from django.contrib.auth import login
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
