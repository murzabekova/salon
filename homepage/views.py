from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        'messages': "first page",
    }
    return render(request, 'homepage/index.html', context)