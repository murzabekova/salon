from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.


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


def signout(request):
    logout(request)
    return redirect('/')


# def registration_view(request):
#     form = RegistrationForm(request.POST or None)
#     if form.is_valid():
#         user = form.save()
#         user.set_password(request.POST['password'])
#         user.save()
#         return redirect('/index/')
#     return render(request, 'accounts/registration.html', {'form': form})
