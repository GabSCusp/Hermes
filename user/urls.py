from user.views import Registrar, UserConfigView, HermesLogOut, list_favoritos 
from django.urls import path, include
from django.contrib.auth.views import PasswordResetView

urlpatterns = [
               path('registrar/', Registrar, name = 'registrar'),
               path('recuperar-senha/',PasswordResetView.as_view() ,name = "recuperar-senha"),
               path('', include('django.contrib.auth.urls')),
               path('perfil/', UserConfigView.as_view(),name = "perfil"),
               path('logout/', HermesLogOut.as_view(), name = "logout"),
               path('perfil/favoritos/', list_favoritos, name = "favoritos")
]
