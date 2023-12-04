from django import forms

class MensagemForm(forms.Form):
    assunto = forms.CharField(max_length=200)
    mensagem = forms.CharField(widget=forms.Textarea)
