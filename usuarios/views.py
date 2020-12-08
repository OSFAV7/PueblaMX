from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

# Create your views here.



class login(LoginView):
    template_name="usuarios/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar seción'
        return context
