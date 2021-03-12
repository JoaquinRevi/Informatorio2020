from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context



def nosotros(request):
	return render(request,"ProyectoPongoApp/nosotros.html")

def ayuda(request):
	return render(request,"ProyectoPongoApp/ayuda.html")

