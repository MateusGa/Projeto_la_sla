#manda isso pro github

from django.urls import path
from .views import *

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("Le_Start/", Index.as_view(), name="Le_Start"),
    path("Sobre_Nos/", Sobre.as_view(), name="sobre"),
    path("Contatos",Contato.as_view(), name="contatos" )
]
