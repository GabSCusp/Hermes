from django import forms
from local.models import Local

class AddLocalForm(forms.ModelForm):
        class Meta:
            model = Local
            fields = ['nome','endereço','descrição','CEP','latitude','longitude','imagem']
            labels = {'nome':'Nome'}
            widgets = {'descrição':forms.Textarea}
