from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import Http404
from post.forms import PostForm
from post.models import Category, Post


# import datetime

# Create your views here.

def post(request):
    context = {
        'news': Post.objects.all().order_by('-date'),
        'categories': Category.objects.all(),
    }
    return render(request, 'post/post.html', context)


@login_required(login_url='/error/')
def create(request):
    if request.user.is_staff:
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/post')
        return render(request, 'post/create.html', {'form': form})
    return redirect('/error/')


@login_required(login_url='/error/')
def edit(request, post_id):
    if request.user.is_staff:
        post = Post.objects.get(id=post_id)
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/post')
        return render(request, 'post/create.html', {'form': form})
    return redirect('/error/')


@login_required(login_url='/error/')
def delete(request, post_id):
    if request.user.is_staff:
        post = Post.objects.get(id=post_id)
        post.delete()
        return redirect('/post')
    return redirect('/error/')
