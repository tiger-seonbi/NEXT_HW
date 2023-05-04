from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'Blog/home.html', {'posts':posts})

@login_required(login_url='/accounts/login')
def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
        )
        return redirect('Blog:home')
    return render(request, 'Blog/new.html')

@login_required(login_url='/accounts/login')
def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.all()
    if request.method == 'POST':
        new_comment = Comment.objects.create(
            content = request.POST['content'],
            post = post,
            author = request.user,
        )
        return redirect('Blog:detail', post_id)
    return render(request, 'Blog/detail.html', {'post':post, 'comments':comments})

def update(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        Post.objects.filter(pk=post_id).update(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('Blog:detail', post_id)
    return render(request, 'Blog/update.html', {'post':post})

def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()

    return redirect('Blog:home')