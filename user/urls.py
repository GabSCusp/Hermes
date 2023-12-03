from user.views import Registrar
from django.urls import path, include
from django.contrib.auth.views import PasswordResetView

urlpatterns = [
               path('registrar/', Registrar, name = 'registrar'),
               path('recuperar-senha/',PasswordResetView.as_view() ,name = "recuperar-senha"),
               path('', include('django.contrib.auth.urls')),
]
