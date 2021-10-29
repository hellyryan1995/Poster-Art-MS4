from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .forms import CommentForm
from .models import Post, Comment
# Create your views here.


def blog(request):
    '''A view to show the blog page '''

    posts = Post.objects.all()
    template = "blog/blog.html"
    context = {
        'posts': posts,
    }
    
    return render(request, template, context)


def post_detail(request, slug):
    '''A view to show the specific post in detail '''

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            form.save()
            messages.success(request, "Your comment has been added.")
            return redirect('post_detail', slug=post.slug)
        else:
            messages.error(request,
                        "Error adding your comment please try again")
            return redirect('post_detail', slug=post.slug)

    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    template = "blog/post_detail.html"
    context = {
        'post': post,
        'form': form,
        'comments': comments,
    }

    return render(request, template, context)
