from django.shortcuts import render
from slider.models import Slider

# Create your views here.


def show(request):
    context = {
        'slides': Slider.objects.all()
    }
    return render(request, 'slider/show.html', context)
