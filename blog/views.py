from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author, Comment
from django.utils import timezone
from django.db.models import Count

# Create your views here.

def home(request):

    num_post = Post.objects.all().count()
    num_author = Author.objects.all().count()
    #most_liked = Post.objects.all().order_by((Count('likes')))[0]
    most_liked = Post.objects.annotate(Count('likes'))
    context = {
        'num_post' : num_post,
        'num_author' : num_author,
        'most_liked' : most_liked
    }

    return render(request, 'blog/home.html', context=context)

def index(request):
    
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }

    return render(request, 'blog/index.html', context=context)

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts' : posts} )

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'blog/author_detail.html', {'author': author})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/author_list.html', {'authors': authors})
