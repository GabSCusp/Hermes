from django.urls import path
from local.views import LocalListView, adicionar_local

urlpatterns = [
    path('local/', LocalListView.as_view(), name = 'local'),
    path("local/addlocal", adicionar_local, name = "addlocal"),
]
