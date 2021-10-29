from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .forms import CommentForm, Post, PostForm
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


def post_detail(request, post_id):
    '''A view to show the specific post in detail '''

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            form.save()
            messages.success(request, "Your comment has been added.")
            return redirect(reverse('post_detail', args=[post_id]))
        else:
            messages.error(request,
                        "Error adding your comment please try again")
            return redirect(reverse('post_detail', args=[post_id]))

    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    template = "blog/post_detail.html"
    context = {
        'post': post,
        'form': form,
        'comments': comments,
    }

    return render(request, template, context)


def add_post(request):
    """ Add a post to the store """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a new post!')
            return redirect(reverse('add_post'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm()
        
    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
