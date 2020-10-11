from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

# Create your views here.



class login(LoginView):
    template_name="usuarios/login.html"

