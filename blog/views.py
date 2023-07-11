from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author, Comment
from django.utils import timezone
from django.db.models import Count
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def home(request):

    num_post = Post.objects.all().count()
    num_author = Author.objects.all().count()
    most_liked = (Post.objects
    .values('id')
    .annotate(count=Count('likes'))
    .order_by()[0]
    )
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_post' : num_post,
        'num_author' : num_author,
        'most_liked' : most_liked,
        'num_visits': num_visits,
    }

    return render(request, 'blog/home.html', context=context)

def index(request):
    
    return render(request, 'registration/login.html')

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

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create(username=username,email=email,password=password)          
    return render(request, 'registration/login.html')

def login(request):
    pass