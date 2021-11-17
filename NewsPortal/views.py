from django.views.generic import ListView, DetailView  
from .models import Category, Author, Post, PostCategory, Comment
 
 
class PostList(ListView):
    model = Post
    template_name = 'news.html' 
    context_object_name = 'news' 
    queryset = Post.objects.order_by('-created')


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html' 
    context_object_name = 'news'