from rest_framework import serializers
from local.models import Local
from produtos.models import Produto, Review

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['name','preço','Local', 'poster_url']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['author', 'text', 'likes', 'produto']

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ['nome', 'latitude', 'longitude', 'status', 'CEP', 'endereço', 'descrição', 'imagem' ]
