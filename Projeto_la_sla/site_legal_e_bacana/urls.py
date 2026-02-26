#manda isso pro github

from django.urls import path
from .views import Index

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("Parte_1", Index.as_view(), name="Le_Start")
]
