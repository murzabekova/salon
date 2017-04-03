from django.shortcuts import render
from post.models import Post, Category
# import datetime

# Create your views here.

def post(request):
    context = {
        'news': Post.objects.all().order_by('-date'),
        'categories': Category.objects.all()
    }
    return render(request, 'post/post.html', context)
