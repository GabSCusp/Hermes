from django.forms import ModelForm
from .models import Produto, Review

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = [
            'name',
            'preço',
            'Local',
            'poster_url',
        ]
        labels = {
            'name': 'Produto',
            'preço': 'Preço',
            'poster_url': 'URL do Poster',
        }
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        labels = {'text': 'Resenha'}

