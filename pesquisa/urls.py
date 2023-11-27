from django.urls import path
from pesquisa.views import HermesResultPage

urlpatterns = [
    path('', HermesResultPage.as_view(), name="pesquisa"),
]
