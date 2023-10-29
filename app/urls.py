from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.carregarPagina, name='login'),
    #path('paginaConectado/', views.paginaConectado, name='paginaConectado'),
]
