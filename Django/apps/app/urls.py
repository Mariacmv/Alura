from django.urls import path
from apps.app.views import \
    index, imagem, buscar, nova_imagem, editar_imagem, deletar_imagem, filtro #para ter mais espaço

urlpatterns = [
    path('', index, name='index'), #determino um nome a url
    path('imagem/<int:foto_id>', imagem, name='imagem'), #faz o mesmo com o arquivo imagem. Passo esse nome e devolvo ao html para que ele entenda a página
    path("buscar/", buscar, name="buscar"),
    path('nova_imagem/', nova_imagem, name='nova_imagem'),
    path('editar_imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
    path('deletar-imagem/<int:foto_id>', deletar_imagem, name='deletar_imagem'),
    path('filtro/<str:categoria>', filtro, name='filtro')
]#lista dos caminhos