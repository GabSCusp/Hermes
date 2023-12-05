from django import forms
from local.models import Local

class AddLocalForm(forms.ModelForm):
        class Meta:
            model = Local
            fields = ['nome']
            labels = {'nome':'Nome'}
