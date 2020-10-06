from django.shortcuts import render, HttpResponse

# Create your views here.


def asistencia(request):

    return render(request, "ControlAsistencia/lista.html")