from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author, Comment
from django.utils import timezone
from django.db.models import Count
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, AuthorForm


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
    
    return render(request, 'blog/index.html')

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
        user_form = UserRegistrationForm(request.POST)
        author_from = AuthorForm(request.POST)
        if (user_form.is_valid() and author_from.is_valid()):
            user_form.save()
            author_from.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('home') #change via login page
    else:
        user_form = UserRegistrationForm()
        author_from = AuthorForm()

    context = {'user_form': user_form,
               'author_from': author_from,
               }
    return render(request, 'registration/register.html', context)

def login(request):
    pass