from django.urls import path
import api.views as v

urlpatterns = [
    path('local/<int:pk>/', v.LocalDetalhe.as_view()),
    path('local/', v.LocalLista.as_view()),
    path('reviews/<int:pk>/', v.ReviewDetalhe.as_view()),
    path('reviews/', v.ReviewLista.as_view()),
    path('produtos/<int:pk>/', v.ProdutoDetalhe.as_view()),
    path('produtos/', v.ProdutoLista.as_view()),
]

