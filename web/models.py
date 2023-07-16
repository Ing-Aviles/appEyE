from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TipoEmpresa(models.Model):
    carrera_Empresa = models.CharField(max_length=30)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.carrera_Empresa
    
class Empresa(models.Model):
    tipo_Empresa = models.ForeignKey(TipoEmpresa, on_delete=models.RESTRICT)
    nombre_Empresa = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='empresa', blank=True)
    cupos = models.IntegerField(default=1)
    
    def __str__(self):
        return  self.nombre_Empresa
    
class Alumno(models.Model):
    matricula = models.OneToOneField(User,on_delete=models.RESTRICT)
    genero = models.CharField(max_length=12)
    carrera = models.CharField(max_length=30)
    correoIns = models.EmailField()
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    whatsApp = models.CharField(max_length=20)
    edad = models.CharField(max_length=10)

    def __str__(self):
        return self.matricula
    
class EmpresaR(models.Model):

    ESTADO_CHOICES = (
        ('0','Pendiente'),
        ('1','Aceptado')
    )

    matricula = models.ForeignKey(Alumno, on_delete=models.RESTRICT)
    estado = models.CharField(max_length=1,default=0, choices=ESTADO_CHOICES)
    nro_Solicitud = models.CharField(max_length=50)
    cupos = models.IntegerField(default=1)
    
    def __str__(self):
        return self.nro_Solicitud
    


    

