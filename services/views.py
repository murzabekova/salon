from django.shortcuts import render
from fillials.models import FillialServices, Fillials
from services.models import Services
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def list_of_services(request):
    content = {
        'services': Services.objects.all(),
    }
    return render(request, 'services/list.html', content)


def list_by_service(request, service_id):
    service = Services.objects.get(id=service_id)
    fillialservices = service.fillialservices_set.all()
    # values_list('fillial').distinct()
    content = {
        'services': fillialservices,
    }
    return render(request, 'services/list_by.html', content)
