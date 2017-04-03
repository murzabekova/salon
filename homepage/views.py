import datetime

from django.shortcuts import render

from post.models import Post
from slider.models import Slider


# Create your views here.


def index(request):
    slides = Slider.objects.all()
    context = {
    	'posts': Post.objects.all().order_by('-date'),
        'messages': "first page",
        'slides': slides,
        'count': range(len(slides)),
    }
    return render(request, 'homepage/index.html', context)
