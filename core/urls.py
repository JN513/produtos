from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('cria_produto', views.cria_produto, name='cria_produtos'),
    path('cria_categoria', views.cria_categoria, name='cria_categoria'),
    path('cria_tipo', views.cria_tipo, name='cria_tipo'),
    path('muda_estoque', views.muda_estoque, name='muda_estoque'),
    path('search/', views.search, name='search')
]