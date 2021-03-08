from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
	filtro = models.CharField(max_length = 20 )
	creado = models.DateTimeField(auto_now_add = True)
	actualizado = models.DateTimeField(auto_now = True)

	class Meta:
		verbose_name = "categoria"
		verbose_name_plural = "categorias"

	def __str__(self):
		return self.filtro

class Post(models.Model):
	titulo = models.CharField(max_length = 20)
	contenido = models.CharField(max_length = 300)
	autor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts')
	imagen = models.ImageField(upload_to = "postmedia")
	categorias = models.ManyToManyField(Categoria)
	creado = models.DateTimeField(auto_now_add = True)
	actualizado = models.DateTimeField(auto_now = True)

	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Posts"


	def __str__(self):
		return self.titulo	



