from django.urls import path
from local.views import LocalListView

urlpatterns = [
    path('', LocalListView.as_view(), name = 'local')
]
