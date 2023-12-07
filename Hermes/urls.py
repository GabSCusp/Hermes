from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('pesquisa/',include('pesquisa.urls')),
    path('admin/', admin.site.urls),
    path('',include('local.urls')),
    path('',include('mensagens.urls')),
    path('',include('user.urls')),
    path('produtos/', include('produtos.urls')),
    path('api/v1/', include('api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
