from django.shortcuts import render,redirect
from post.models import Post, Categoria
from django.views.generic import CreateView
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required



# Create your views here.

def inicio(request):
	posts = Post.objects.all()
	return render(request,"posts/index.html", {"posts": posts})

@login_required
def PostCreation(request):
	if request.method == 'POST':
		form = PostForm(request.POST,request.FILES)
		if form.is_valid():
			post = form.save(commit = False)
			post.autor = request.user
			post.creacion = timezone.now()
			post.save()
			return redirect('inicio')
	else:
		form = PostForm()
	return render(request, 'posts/crearpost.html', {'form': form})

def categoria(request, categoria_id):
	categoria = Categoria.objects.get(id = categoria_id)
	posts = Post.objects.filter(categorias = categoria)
	return render(request, "posts/categorias.html", {'categoria': categoria, 'posts': posts })