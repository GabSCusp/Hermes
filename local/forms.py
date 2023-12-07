from django import forms
from local.models import Local

class AddLocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nome', 'endereço', 'descrição', 'CEP', 'latitude', 'longitude', 'imagem']
        labels = {'nome': 'Nome'}
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'descrição': forms.Textarea(attrs={'placeholder': 'Descrição'}),
            'endereço': forms.TextInput(attrs={'placeholder': 'Endereço'}),
            'CEP': forms.TextInput(attrs={'placeholder': 'CEP'}),
            'latitude': forms.TextInput(attrs={'placeholder': 'Latitude'}),
            'longitude': forms.TextInput(attrs={'placeholder': 'Longitude'}),
            'imagem': forms.ClearableFileInput(attrs={'placeholder': 'Imagem'}),
        }
