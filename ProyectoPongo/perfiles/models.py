from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	imagenu = models.ImageField(upload_to = "perfilesmedia")
	biografia = models.CharField(max_length = 300)

	def __str__(self):
		return f'Perfil de {self.user.username}'

