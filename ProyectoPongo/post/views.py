from django.shortcuts import render,redirect
from post.models import Post
from django.views.generic import CreateView


# Create your views here.

def inicio(request):
	posts = Post.objects.all()
	return render(request,"posts/index.html", {"posts": posts})



