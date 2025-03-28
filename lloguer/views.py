# lloguer/views.py
from django.shortcuts import render
from lloguer.models import Automobil

def autos(request):
    automoviles = Automobil.objects.all()

    # Pasar los automóviles al template
    return render(request, 'lloguer/autos.html', {'automoviles': automoviles})
