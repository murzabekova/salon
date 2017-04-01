from django.shortcuts import render
from slider.models import Slider

# Create your views here.


def index(request):
    slides = Slider.objects.all()
    context = {
        'messages': "first page",
        'slides': slides,
        'count': range(len(slides)),
    }
    return render(request, 'homepage/index.html', context)
