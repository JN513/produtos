from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    #path('search/', views.search, name='search'),
    path('confirm/<str:token>', views.confirma_email, name="confirma")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)