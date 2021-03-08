from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as salir
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as ingresar
from perfiles.forms import RegistroUsuario
from perfiles.models import Usuario

def register(request):
    form = RegistroUsuario()
    if request.method == "POST":
        form = RegistroUsuario(data=request.POST)
        if form.is_valid():
            user = form.save() 
            if user is not None:
                ingresar(request, user)
                return redirect('/')

    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    return render(request, "registro.html", {'form': form})

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                ingresar(request, user)
                return redirect('/')

    form.fields['username'].help_text = None   
    return render(request, "login.html", {'form': form})


def logout(request):
	salir(request)

	return redirect("/")

def perfil(request):
    perfil = Usuario.objects.all()
    return render(request,"perfil.html", {"perfil": perfil})
