from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')