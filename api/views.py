from rest_framework import generics
from .serializers import ProdutoSerializer, ReviewSerializer, LocalSerializer 
from local.models import Local
from produtos.models import Produto, Review

class ProdutoLista(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ReviewLista(generics.ListCreateAPIView):
    queryset = Review.objects.all
    serializer_class = ReviewSerializer

class ReviewDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class LocalLista(generics.ListCreateAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class LocalDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
