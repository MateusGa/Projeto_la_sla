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

     #URL para Subtarefas
    path("cadastrar/subtarefas/", SubtarefaCreate.as_view(), name="subtarefas_create"),
    path("listar/subtarefas/", SubtarefaList.as_view(), name="subtarefas_listar"),
    path("editar/subtarefas/<int:pk>/", SubtarefaUpdate.as_view(), name="subtarefas_update"),
    path("excluir/subtarefas/<int:pk>/", SubtarefaDelete.as_view(), name="subtarefas_delete"),
    path("ver/subtarefas/<int:pk>/", SubtarefaDetail.as_view(), name="subtarefas_ver"),


    #URL para Anexos
    path("cadastrar/anexos/", AnexoCreate.as_view(), name="anexos_create"),
    path("listar/anexos/", AnexoList.as_view(), name="anexos_listar"),
    path("editar/anexos/<int:pk>/", AnexoUpdate.as_view(), name="anexos_update"),
    path("excluir/anexos/<int:pk>/", AnexoDelete.as_view(), name="anexos_delete"),
    path("ver/anexos/<int:pk>/", AnexoDetail.as_view(), name="anexos_ver"),


    #URL para Lembretes
    path("cadastrar/lembretes/", LembreteCreate.as_view(), name="lembretes_create"),
    path("listar/lembretes/", LembreteList.as_view(), name="lembretes_listar"),
    path("editar/lembretes/<int:pk>/", LembreteUpdate.as_view(), name="lembretes_update"),
    path("excluir/lembretes/<int:pk>/", LembreteDelete.as_view(), name="lembretes_delete"),
    path("ver/lembretes/<int:pk>/", LembreteDetail.as_view(), name="lembretes_ver"),


    #URL para Participantes
    path("cadastrar/participantes/", ParticipanteCreate.as_view(), name="participantes_create"),
    path("listar/participantes/", ParticipanteList.as_view(), name="participantes_listar"),
    path("editar/participantes/<int:pk>/", ParticipanteUpdate.as_view(), name="participantes_update"),
    path("excluir/participantes/<int:pk>/", ParticipanteDelete.as_view(), name="participantes_delete"),
    path("ver/participantes/<int:pk>/", ParticipanteDetail.as_view(), name="participantes_ver"),
]
