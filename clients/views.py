from django.shortcuts import render, redirect
from fillials.models import Fillials, FillialServices
from clients.forms import ClientsForm, ActivationForm
from clients.email import SubscriptionView
from clients.models import Clients
from profiles.models import MasterProfile, MasterService
from schedule.models import Calendar
# Create your views here.


def contacts(request, id_services):
    form = ClientsForm(request.POST or None)
    if form.is_valid():
        client = form.save(commit=False)
        number = SubscriptionView(client.email)
        services = FillialServices.objects.get(id=id_services)
        print(id_services)
        client.service = services
        client.number = number
        client.active = False
        # client.master = master
        # client.shedule
        client.save()
        print(client.id)
        return redirect('/clients/activation/%s' % client.id)
    return render(request, 'clients/contacts.html', {'form': form})


def activation(request, id_client):
    """ """
    number = ActivationForm(request.POST or None)
    client = Clients.objects.get(id=id_client)
    print(client.number)
    if number.is_valid():
        subject = number.cleaned_data['your_kod']
        print(subject)
        if client.number == subject:
            client.active = True
            client.save()
            return redirect('/end/')
        # return redirect('')
    return render(request, 'clients/activation.html', {'number': number})



def list_of_fillials(request):
    context = {
        'salons': Fillials.objects.all().filter(active=True),
    }
    return render(request, 'clients/list_of_fillials.html', context)



def list_of_services(request,id_fillials):
    services = FillialServices.objects.all().filter(fillial=id_fillials)
    return render(request, 'clients/list_of_services.html', {'services': services})



def list_of_masters (request,id_services):
    services = MasterService.objects.filter(service_id=id_services)
    l=[]
    for i in MasterProfile.objects.all():
        counter = 0
        for j in services:
            for k in j.profile.all():
                if i.id == k.id:
                    counter=1
        if counter == 0:
            l.append(i.id)
    print(l)
    mp = MasterProfile.objects.exclude(id__in = l)
    context = {
        'masters': mp
    }
    return render(request, 'clients/list_of_masters.html', context)

def event(request,id_master):
    # calendar = Calendar.objects.get(slug=id_master)
    return render(request, 'clients/event.html', {'user': id_master})
