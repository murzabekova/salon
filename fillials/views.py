from django.shortcuts import render, redirect
from fillials.models import Fillials
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator
from project.roles import Administrator
from fillials.forms import FillialsForm
# from rolepermissions.verifications import has_permission, has_role

# Create your views here.


@login_required(login_url='/error/')
@has_role_decorator('administrator')
def salon(request):
    salon, created = Fillials.objects.get_or_create(user=request.user)
    context = {
        'salon': salon,
        'username': request.user,
    }
    return render(request, 'fillials/salon.html', context)


def list_of_salons(request):
    pass


def list_of_services(request):
    pass


@login_required(login_url='/error/')
@has_role_decorator('administrator')
def edit_salon(request):
    form = FillialsForm(request.POST or None, request.FILES or None, instance=Fillials.objects.get(user=request.user))
    if form.is_valid():
        salon = form.save(commit=False)
        salon.user = request.user
        salon.save()
        return redirect('/')
    return render(request, 'fillials/edit_salon.html', {'form': form})
