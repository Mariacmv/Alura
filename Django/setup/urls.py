from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), #rota principal
    path('', include('apps.app.urls')), #chamo a função view - isolo o index
    path('', include('apps.usuarios.urls')),
] 

if settings.DEBUG: #se a aplicação está rodando
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)