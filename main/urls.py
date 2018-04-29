from django.urls import re_path, path
from .import views

# We are adding a URL called /home
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    re_path(r'^cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    re_path(r'^registrar/', views.registrar, name='registrar'),
    re_path(r'^principal/', views.principal, name='principal'),
    re_path(r'^saldo', views.saldo, name='saldo'),
    re_path(r'^transferir/', views.transferir, name='transferir'),
    re_path(r'^debito_credito/', views.debito_credito, name='debito_credito'),
]