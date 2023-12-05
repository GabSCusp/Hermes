from django.urls import path

from . import views

app_name = 'produtos'
urlpatterns = [
    path('', views.list_produtos, name='Produtos'),
    path('search/', views.search_produtos, name='search'),
    path('create/', views.create_produto, name='create'),
    path('<int:produto_id>/review/', views.create_review, name='review'),
    path('lists/', views.ListListView.as_view(), name='lists'),
    path('lists/create', views.ListCreateView.as_view(), name='create-list'),
    path('<int:produto_id>/', views.detail_produto, name='detail'),
]