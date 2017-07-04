from django.shortcuts import render, redirect
from profiles.models import MasterProfile, MasterService
from profiles.forms import ProfileForm, MasterServiceForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def profile(request):
    profile, created = MasterProfile.objects.get_or_create(user=request.user)
    try:
        service = MasterService.objects.get(profile=profile)
    except ObjectDoesNotExist:
        service = ''
    context = {
        'profile': profile,
        'service': service,
    }
    return render(request, 'profiles/profile.html', context)


def edit_profile(request):
    form = ProfileForm(request.POST or None, request.FILES or None,
                       instance=MasterProfile.objects.get(user=request.user))
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect('/')
    return render(request, 'profiles/edit_profile.html', {'form': form})


def add_service(request):
    form = MasterServiceForm(request.POST or None)
    if form.is_valid():
        service = form.save(commit=False)
        service.profile = MasterProfile.objects.get(user=request.user)
        service.save()
        return redirect('/')
    return render(request, 'profiles/add_service.html', {'form': form})
