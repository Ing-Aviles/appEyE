from django.db import models

# Create your models here.
class TipoEmpresa(models.Model):
    carrera_Empresa = models.CharField(max_length=30)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.carrera_Empresa
    
class Empresa(models.Model):
    tipo_Empresa = models.ForeignKey(TipoEmpresa, on_delete=models.RESTRICT)
    nombre_Empresa = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='empresa', blank=True)
    cupos = models.IntegerField(default=1)
    
    def __str__(self):
        return  self.nombre_Empresa
    

    

