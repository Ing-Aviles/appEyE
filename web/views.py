from django.shortcuts import render
from . models import TipoEmpresa, Empresa

# Create your views here.
"""vistas alumno del catalogo de empresas"""

def catalogoEmpresas(request):
    listaEmpresa = Empresa.objects.all()
    listaTipoEmpresa = TipoEmpresa.objects.all()

    context ={
        'empresa':listaEmpresa,
        'tipo_Empresa': listaTipoEmpresa
        
    }
    return render(request,'catalogoEmpresas.html',context)

def empresasPorCarrera(request, tipo_Empresa_id):
    objTipoEmpresa = TipoEmpresa.objects.get(pk = tipo_Empresa_id)
    ListaEmpresa = objTipoEmpresa.empresa_set.all()

    listaTipoEmpresa = TipoEmpresa.objects.all()

    context = {
        'empresa':ListaEmpresa,
        'tipoEmpresa': listaTipoEmpresa
    }
    
    return render(request,'catalogoEmpresas.html',context)

def index(request):

    return render(request, 'index.html')
