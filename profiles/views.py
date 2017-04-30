from django.shortcuts import render, redirect
from profiles.models import MasterProfile
from profiles.forms import ProfileForm
# Create your views here.


def profile(request):
    profile, created = MasterProfile.objects.get_or_create(user=request.user)
    context = {
        'profile': profile,
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
