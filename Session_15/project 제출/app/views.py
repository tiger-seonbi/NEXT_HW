import json

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import Comment, Post, Like

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


@login_required(login_url='/registration/login')
def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            author=request.user
        )
        return redirect('detail', new_post.pk)
    return render(request, 'new.html')


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    likes = Like.objects.filter(post=post)
    if (request.method == 'POST'):
        Comment.objects.create(
            post=post,
            content=request.POST['content'],
            author=request.user
        )
        return redirect('detail', post_pk)

    return render(request, 'detail.html', {'post': post})


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('detail', post_pk)

    return render(request, 'edit.html', {'post': post})


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')


def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)


def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) > 0):
            error = 'username이 이미 존재합니다'
            return render(request, 'registration/signup.html', {'error': error})

        new_user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        auth.login(
            request,
            new_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect('home')

    return render(request, 'registration/signup.html')


def login(request):
    if (request.method == 'POST'):
        found_user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', {'error': error})
        auth.login(
            request,
            found_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect(request.GET.get('next', '/'))
    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')

def mypage(request):
    posts = Post.objects.all()
    return render(request, 'mypage.html', { "posts":posts  })

@csrf_exempt
def like(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        post_pk = request_body['post_pk']
        post = Post.objects.get(pk=post_pk)
        user_like = Like.objects.filter(user=request.user, post=post)

        if (len(user_like) > 0):
            user_like.delete()
        else:
            Like.objects.create(
                    post=post,
                    user=request.user
            )

        response = {
            'like_count': post.likes.count(),
        }
        return HttpResponse(json.dumps(response))
    
@csrf_exempt
def comment(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        comment = request_body['comment']
        str_comment = ''.join(comment)
        post_pk = request_body['post_pk']
        post = Post.objects.get(pk=post_pk)

        new_comment = Comment.objects.create(
            post = post,
            author = request.user,
            content = str_comment,
        )

        response = {
            'content' : str_comment,
            'post_pk' : post_pk,
            'comment_pk' : new_comment.pk,
        }
        return HttpResponse(json.dumps(response))

@csrf_exempt
def comment_delete(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        comment_pk = request_body['id']
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()

        response = {
            'comment-pk' : comment.pk,
        }
        return HttpResponse(json.dumps(response))