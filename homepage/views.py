from django.shortcuts import render
<<<<<<< HEAD
from post.models import Post
import datetime
=======
from slider.models import Slider
>>>>>>> 6ce8711f0a3e93560711b73a7a07eb80110c5d37

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
