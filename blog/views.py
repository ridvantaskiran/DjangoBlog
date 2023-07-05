from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author, Comment
from django.utils import timezone

# Create your views here.

def index(request):
    
    posts = Post.objects.all()

    context = {
        'posts' : posts
    }

    return render(request, 'blog/index.html', context=context)