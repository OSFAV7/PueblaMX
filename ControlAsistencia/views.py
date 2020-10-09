from django.shortcuts import render, HttpResponse
from .models import Empleados
from .forms import formempleado
from django.views.generic import TemplateView, CreateView

# Create your views here.

class agreemple(CreateView):
    model = Empleados
    form_class = formempleado
    template_name= "ControlAsistencia/lista.html"


