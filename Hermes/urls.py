from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path('pesquisa/',include('pesquisa.urls')),
    path('admin/', admin.site.urls),
    path('local/',include('local.urls')),
    path('',include('mensagens.urls')),
    path('',include('user.urls')),
]
