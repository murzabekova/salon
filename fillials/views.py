from django.shortcuts import render, redirect
from fillials.models import Fillials, Gallery
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator
from project.roles import Administrator
from fillials.forms import FillialsForm, GalleryForm
# from rolepermissions.verifications import has_permission, has_role

# Create your views here.


@login_required(login_url='/error/')
@has_role_decorator('administrator')
def salon(request):
    salon, created = Fillials.objects.get_or_create(user=request.user)
    gallery = Gallery.objects.all().filter(fillial=salon)
    context = {
        'salon': salon,
        'username': request.user,
        'gallery': gallery,
    }
    return render(request, 'fillials/salon.html', context)


def list_of_salons(request):
    context = {
        'salons': Fillials.objects.all().filter(active=True),
    }
    return render(request, 'fillials/list_of_salons.html', context)


def list_of_services(request):
    pass


@login_required(login_url='/error/')
@has_role_decorator('administrator')
def edit_salon(request):
    context = {}
    form = FillialsForm(request.POST or None, request.FILES or None,
                        instance=Fillials.objects.get(user=request.user), prefix="form")
    # gallery = GalleryForm(request.POST or None, request.FILES or None, prefix="gallery")
    context = {
        'form': form,
        # 'gallery': gallery,
    }
    if form.is_valid():  # and gallery.is_valid():
        salon = form.save(commit=False)
        salon.user = request.user
        salon.save()
        # image = gallery.save(commit=False)
        # image.fillial = salon
        # image.save()
        return redirect('/')
    return render(request, 'fillials/edit_salon.html', context)


@login_required(login_url='/error/')
@has_role_decorator('administrator')
def create_salon(request):
    form = FillialsForm(request.POST or None, request.FILES or None, instance=Fillials.objects.get(user=request.user))
    context = {
        'form': form,
    }
    if form.is_valid():
        salon = form.save(commit=False)
        salon.user = request.user
        salon.save()
        return redirect('/')
    return render(request, 'fillials/create_salon.html', context)


def list_of_salons_to_activate(request):
    context = {
        'salons': Fillials.objects.exclude(title__isnull=True).exclude(title__exact=''),
    }
    return render(request, 'fillials/list_of_salons_to_activate.html', context)


@login_required(login_url='/error/')
def activate_salon(request, salon_id):
    if request.user.is_staff:
    # try:
    # except:
        fillial = Fillials.objects.get(id=salon_id)
        fillial.active = True
        fillial.save()
        return redirect('/fillial/list_of/')
    return redirect('/error/')
