from django.db import models

# Create your models here.
class Empleados(models.Model):
    nosocial=models.CharField('Numero social',primary_key= True, unique= True, max_length=30)
    nombre=models.CharField('Nombres del empleado',max_length=30)
    apellidos=models.CharField('Apellidos del empleado',max_length=40)
    cargo=models.CharField('Cargo que desempeña',max_length=30)
    telefono=models.CharField('Telefono de contacto',max_length=10)
    asistencia=models.BooleanField('Asistencia del dia', default= False)

    class Meta:
        verbose_name= 'Empleado'
        verbose_name_plural= 'Empleados'
    
    def __str__(self):
        return self.nombre
        
class asistencias (models.Model):
    empleado= models.ForeignKey(Empleados, on_delete=models.CASCADE)
    fecha= models.DateField('Fecha de asistencia')

    class Meta():
        verbose_name= 'Asitencia'
        verbose_name_plural= 'Asistencias'
    
    def __str__(self):
        return '{} {}'.format(self.empleado, self.fecha)

