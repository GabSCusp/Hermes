from django.forms import ModelForm

from local.models import Local

class FormPesquisaLocal(ModelForm):
    class Meta:
        model = Local
        fields = ['nome',]
        labels = {'nome':'nome',}
