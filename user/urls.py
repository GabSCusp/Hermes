from user.views import LoginPageView, Registrar
from django.urls import path

urlpatterns = [path('login/', LoginPageView.as_view(), name = 'login'),
               path('registrar/', Registrar, name = 'registrar'),
]
