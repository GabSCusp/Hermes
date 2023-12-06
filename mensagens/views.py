from django.shortcuts import render, redirect
from mensagens.models import MensagemParaSuporte
from mensagens.forms import MensagemForm 

def enviar_mensagem(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = MensagemForm(request.POST)
            if form.is_valid():
                mensagem = MensagemParaSuporte(assunto = form.cleaned_data['assunto'],
                                                mensagem = form.cleaned_data['mensagem'],
                                               ) 
                mensagem.save()
                return redirect('home') #TODO: talvez adicionar uma página de agradecimento
        form = MensagemForm()
        return render(request, 'mensagens/fale_conosco.html', {'form':form})
    return redirect('login')
