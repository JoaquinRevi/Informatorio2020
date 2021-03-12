from django.shortcuts import render
from .forms import FormularioContacto

# Create your views here.

def contactanos(request):
	form = FormularioContacto()
	return render(request,"contactanos.html", {'conform': form})	