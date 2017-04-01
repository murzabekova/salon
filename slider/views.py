from django.shortcuts import render
from slider.models import Slider

# Create your views here.


def show(request):
    slides = Slider.objects.all()

    context = {
        'slides': slides,
        'count': range(len(slides)),
    }
    return render(request, 'slider/show.html', context)
