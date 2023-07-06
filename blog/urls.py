from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('Post/<int:pk>', views.post_detail, name='post_detail'),
    path('Bloggers/', views.index, name='index'),
    path('PostList', views.post_list, name='post_list'),
    path('Authors', views.author_list, name='author_list'),
    path('Author/<int:pk>', views.author_detail, name='author_detail')
]