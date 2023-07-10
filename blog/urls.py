from django.urls import path, re_path
from . import views


urlpatterns = [
    #path("", views.register_request, name="register"),
    path('', views.index, name='index'),
    path('Post/<int:pk>', views.post_detail, name='post_detail'),
    path('PostList', views.post_list, name='post_list'),
    path('Bloggers', views.author_list, name='author_list'),
    path('Author/<int:pk>', views.author_detail, name='author_detail'),
    path('register/', views.register, name='register'),
]