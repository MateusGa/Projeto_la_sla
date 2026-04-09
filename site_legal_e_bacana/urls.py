#manda isso pro github

from django.urls import path
from .views import *

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", Index.as_view(), name="Le_Start"),
    path("Sobre_Nos/", Sobre.as_view(), name="sobre"),
    path("Contatos",Contato.as_view(), name="contatos"),
    path("Modelo", Modelo.as_view(), name="modelo"),

    #URL para Eventos
    path("cadastrar/eventos/", EventoCreate.as_view(), name="eventos_create"),
    path("listar/eventos/", EventoList.as_view(), name="eventos_listar"),
    path("editar/eventos/<int:pk>/", EventoUpdate.as_view(), name="eventos_update"),
    path("excluir/eventos/<int:pk>/", EventoDelete.as_view(), name="eventos_delete"),
    path("ver/eventos/<int:pk>/", EventoDetail.as_view(), name="eventos_ver"),
]
