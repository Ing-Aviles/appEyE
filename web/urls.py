from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registroEmpresa/', views.registroEmpresa, name='registroEmpresa'),
    path('loginEmpresa/',views.loginEmpresa, name='loginEmpresa'),
    path('catalogoEmpresas/',views.catalogoEmpresas,name='catalogoEmpresas'),
    path('empresasPorCarrera/<int:tipo_Empresa_id>', views.empresasPorCarrera,name='empresasPorCarrera'),
    path('formulario/', views.formulario, name='formulario'),
    path('vistaEmpresa/', views.vistaEmpresa, name='vistaEmpresa'),
    
]