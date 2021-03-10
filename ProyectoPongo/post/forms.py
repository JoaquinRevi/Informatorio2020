from django import forms
from .models import Post


class PostForm(forms.ModelForm):
 	class Meta:
 		model = Post
 		fields = ['titulo','contenido','imagenp','categorias']

 		labels = {
 			'titulo': 'titulo',
 			'contenido': 'contenido',
 			'imagenp': 'imagenp',
 			'categorias': 'categorias',
 		}


