from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context
from django.template import loader
# Create your views here.


def inicio(request):
    plantilla= loader.get_template('ecommerce.html')
    renderizar= plantilla.render()
    return HttpResponse(renderizar)