from user.views import Registrar
from django.urls import path, include

urlpatterns = [
               path('registrar/', Registrar, name = 'registrar'),
               path('accounts/', include('django.contrib.auth.urls')),
]
