from django.contrib import admin

# Register your models here.
from .models import TipoEmpresa,Empresa

admin.site.register(TipoEmpresa)
#admin.site.register(Empresa)

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre_Empresa','descripcion','imagen','fecha_registro','cupos')
    list_editable = ('cupos',)