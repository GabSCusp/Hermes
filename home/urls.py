from django.urls import path
from home.views import HermesHomePage

urlpatterns = [
    path('', HermesHomePage.as_view(), name='home')
]
