from django.urls import path
from . import views

app_name = 'veiculos'

urlpatterns = [
    path('', views.home, name='home_page'),
    path('catalogo/', views.lista_veiculos, name='lista_veiculos'),
    path('detalhe/', views.detalhe, name='detalhe_veiculo'), # <-- O nome é este!
]