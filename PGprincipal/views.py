from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Create your views here.



class inicio(TemplateView):
    template_name="PGprincipal/index.html"