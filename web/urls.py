from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogoEmpresas/',views.catalogoEmpresas,name='catalogoEmpresas'),
    path('empresasPorCarrera/<int:tipo_Empresa_id>', views.empresasPorCarrera,name='empresasPorCarrera'),

]