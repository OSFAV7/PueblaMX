from django import forms
from .models import Empleados

class formempleado(forms.ModelForm):
    class Meta():
        model = Empleados
        fields = ['nosocial','nombre', 'apellidos', 'cargo', 'telefono']
        labels = {
            'nosocial': 'Numero social',
            'nombre': 'Nombres', 
            'apellidos': 'Apellidos', 
            'cargo': 'Cargo que desenpeña', 
            'telefono': 'Telefono de contacto',
        }
