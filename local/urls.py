from django.urls import path
from local.views import LocalListView, adicionar_local, LocalDetailView

urlpatterns = [
    path('local/', LocalListView.as_view(), name = 'local'),
    path("local/addlocal/", adicionar_local, name = "addlocal"),
    path('local/<int:pk>/', LocalDetailView.as_view(), name='detalhe_local'),
]
