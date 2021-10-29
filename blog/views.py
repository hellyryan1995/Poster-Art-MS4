from django.shortcuts import render

from .models import Post
# Create your views here.


def blog(request):
    # posts = Post.object.all()
    
    return render(request, 'blog/blog.html')
