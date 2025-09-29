from django.urls import path
from . import views

urlpatterns = [
    path("", views.subir_archivos, name="subir_archivos"),
    path("lista/", views.lista_archivos, name="lista_archivos"),
]