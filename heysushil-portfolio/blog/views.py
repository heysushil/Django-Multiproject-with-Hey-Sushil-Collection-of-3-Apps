from django.shortcuts import render
from blog.models import Post, Category, Comment

# Create your views here.
def blog_index(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, 'blog_index.html', context)