# import datetime

from django.shortcuts import render
from django.http import Http404
from post.models import Post
from slider.models import Slider


# Create your views here.


def index(request):
    slides = Slider.objects.all().filter(display=True)
    context = {
        'posts': Post.objects.all().order_by('-date')[:3],
        'messages': "first page",
        'slides': slides,
        'count': range(len(slides)),
    }
    # print (has_permission(request.user, 'profile'))
    return render(request, 'homepage/index.html', context)


def error(request):
    return render(request, 'homepage/error.html')


def end(request):
    return render(request, 'homepage/end.html')
