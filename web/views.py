from django.shortcuts import render, redirect
from . models import TipoEmpresa, Empresa
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
"""vistas alumno del catalogo de empresas"""
def catalogoEmpresas(request):
    listaEmpresa = Empresa.objects.all()
    listaTipoEmpresa = TipoEmpresa.objects.all()

    context ={
        'empresa':listaEmpresa,
        'tipo_Empresa': listaTipoEmpresa
        
    }
    return render(request,'core/catalogoEmpresas.html',context)

def empresasPorCarrera(request, tipo_Empresa_id):
    objTipoEmpresa = TipoEmpresa.objects.get(pk = tipo_Empresa_id)
    ListaEmpresa = objTipoEmpresa.empresa_set.all()

    listaTipoEmpresa = TipoEmpresa.objects.all()

    context = {
        'empresa':ListaEmpresa,
        'tipoEmpresa': listaTipoEmpresa
    }
    
    return render(request,'core/catalogoEmpresas.html',context)


def index(request):

    return render(request, 'core/index.html')


def formulario(request):

    return render(request, 'core/formulario.html')

def vistaEmpresa(request):
    return render(request, 'core/vistaEmpresa.html')


"""Logins and registers"""

def registroEmpresa(request):

    if request.method == 'POST':
        dataEmpresa = request.POST['nombre_completo']
        """numEmpresa = request.POST['telefono']"""
        correoEmpresa = request.POST['correo_electronico']
        dataPassword = request.POST['password']

        nuevaEmpresa = User.objects.create_user(username=dataEmpresa, email=correoEmpresa,password=dataPassword)
        nuevaEmpresa.save()
        if User is not None:
            login(request, nuevaEmpresa)
            return redirect('loginEmpresa')

    return render(request, 'registration/registroEmpresa.html')

def loginEmpresa(request):

    if request.method == 'POST':
        dataEmpresa = request.POST['username']
        dataPassword = request.POST['password']
        user = authenticate(request, username=dataEmpresa, password=dataPassword)
        if user is not None:
            login(request, user)
            return redirect('vistaEmpresa')  # Redirecciona a la página de inicio
        else:
            messages.error(request, 'Credenciales inválidas')

    return render(request, 'registration/loginEmpresa.html')

def login(request):


    return render(request, 'registration/login.html')
