from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import MasterRegistrationForm, RegistrationForm
from rolepermissions.roles import assign_role
from accounts.permissions import access_create_master
from django.contrib.auth.models import User
from project.roles import Master, Administrator


def signin(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                context = {'login_error': 'Пользователь не найден'}
        else:
            context = {'login_error': 'Пароль или логин неправильны'}
    return render(request, 'accounts/signin.html', context)


@login_required(login_url='/error/')
def signout(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/error/')
def create_master(request):
    if request.user.is_staff or access_create_master(request.user):
        form = MasterRegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST['password'])
            assign_role(user, Master)
            user.save()
            return redirect('/')
        return render(request, 'accounts/signup.html', {'form': form})
    return redirect('/error')


def signup(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.set_password(request.POST['password'])
        user.save()
        return redirect('/')
    return render(request, 'accounts/signup.html', {'form': form})


@login_required(login_url='/error/')
def users_list(request):
    if request.user.is_staff:
        users = User.objects.all().filter(is_staff=False)
        context = {
            'users': users,
        }
        return render(request, 'accounts/users_list.html', context)
    return redirect('/error/')


@login_required(login_url='/error/')
def assign_to_administrator(request, username):
    if request.user.is_staff:
        user = User.objects.get(username=username)
        assign_role(user, Administrator)
        return redirect('/accounts/users/')
    return redirect('/error/')
