from django.contrib import admin
from django.urls import path, include
from Veiculos import views # Importando as views do seu app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('Veiculos.urls')),
    
    # Use 'views.home' se a função no views.py se chamar 'home'
    path('', views.home, name='root_home'), 
]