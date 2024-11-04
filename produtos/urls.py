from django.urls import path
from . import views

urlpatterns = [
    path('ver_produto/', views.ver_produto, name="ver_produto"),
    # path('inserir_produto/', views.inserir_produto, name="inserir_produto"),
    # path('escoher_produto/', views.escolher_produto, name="escolher_produto"),
    # path('visualizar_produto', views.visualizar_produto, name="visualizar_produto")
]