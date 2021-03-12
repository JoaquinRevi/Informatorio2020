from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario


class RegistroUsuario(UserCreationForm):

	class Meta:
		model = User
		fields = [
					'username',
					'first_name',
					'last_name',
					'email',
		]
		labels = {
					'username': 'Nombre de usuario',
					'first_name': 'Nombre',
					'last_name': 'Apellido',
					'email': 'Correo',

		}

class PerfilForm(forms.ModelForm):

	class Meta:
		model = Usuario

		fields = [
					'imagenu',
					'biografia',
		]
