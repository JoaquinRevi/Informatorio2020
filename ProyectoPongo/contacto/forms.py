from django import forms

class FormularioContacto(forms.Form):
	asunto = forms.CharField(label = "asunto", required = True)
	email = forms.CharField(label = "email", required = True)
	contenido = forms.CharField(label = "contenido", required = True)