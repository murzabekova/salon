from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from fillials.models import Fillials, FillialServices

def SubscriptionView(request):
	send_mail('hi', 'Your Email message.', settings.EMAIL_HOST_USER,['cloud1508@mail.ru'], fail_silently=False)



def list_of_fillials(request):
    context = {
        'salons': Fillials.objects.all().filter(active=True),
    }
    return render(request, 'clients/list_of_fillials.html', context)



def list_of_services(request,id_fillials):
    services = FillialServices.objects.all().filter(fillal=id_fillials)
    return render(request, 'clients/list_of_services.html', {'services':services})

# Create your views here.
