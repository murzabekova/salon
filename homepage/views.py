from django.shortcuts import render
from post.models import Post
import datetime

# Create your views here.
def index(request):

    context = {
    	'posts': Post.objects.all().order_by('-date'),
        'messages': "first page",
    }
    return render(request, 'homepage/index.html', context)