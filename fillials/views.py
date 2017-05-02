from django.shortcuts import render, redirect
from fillials.models import Fillials, Gallery, FillialServices
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator
from project.roles import Administrator
from fillials.forms import FillialsForm, GalleryForm, FillialServicesForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from profiles.models import MasterProfile
# from rolepermissions.verifications import has_permission, has_role

# Create your views here.


@login_required(login_url='/error/')
@has_role_decorator('administrator')
def salon(request):
    salon, created = Fillials.objects.get_or_create(user=request.user)
    context = {
        'salon': salon,
        'username': request.user,
        # 'gallery': salon.gallery_set.all(),
        'gallery': Gallery.objects.all().filter(fillial=salon),
        # 'service': salon.fillialservices_set.all(),
        'service': FillialServices.objects.all().filter(fillal=salon),
        # 'masters': salon.masterprofile_set.all(),
        'masters': MasterProfile.objects.all().filter(fillial=salon),
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
    context = {
        'form': form,
    }
    if form.is_valid():  # and gallery.is_valid():
        salon = form.save(commit=False)
        salon.user = request.user
        salon.save()
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


def create_gallery(request):
    salon = Fillials.objects.get(user=request.user)
    gallery = GalleryForm(request.POST or None, request.FILES or None)
    if gallery.is_valid():
        image = gallery.save(commit=False)
        image.fillial = salon
        image.save()
        return redirect('/fillial/')
    return render(request, 'fillials/edit_salon.html', {'form': gallery})


def delete_gallery(request, id_image):
    try:
        post = Gallery.objects.get(id=id_image)
        post.delete()
        return redirect('/fillial/')
    except ObjectDoesNotExist():
        raise Http404


def edit_gallery(request, id_image):
    gallery = Gallery.objects.get(id=id_image)
    form = GalleryForm(request.POST or None, request.FILES or None, instance=gallery)
    if form.is_valid():
        form.save()
        return redirect('/fillial/')
    return render(request, 'fillials/edit_salon.html', {'form': form})


def create_service(request):
    salon = Fillials.objects.get(user=request.user)
    if salon is not None:
        form = FillialServicesForm(request.POST or None)
        if form.is_valid():
            service = form.save(commit=False)
            service.fillal = salon
            service.save()
            return redirect('/fillial/')
    return render(request, 'fillials/edit_salon.html', {'form': form})


def salon_detail(request, salon_id):
    salon = Fillials.objects.get(id=salon_id)
    if salon is not None:
        context = {
            'salon': salon,
            'gallery': Gallery.objects.all().filter(fillial=salon),
            'service': FillialServices.objects.all().filter(fillal=salon),
            'masters': salon.masterprofile_set.all(),
        }
    return render(request, 'fillials/salon_for_clients.html', context)
