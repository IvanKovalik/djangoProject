from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.messages import error


def index_page_view(request):
    context = {}
    return render(request, 'index.html', context=context)


def registration_page_view(request):
    registration_form = CustomUserCreationForm()

    if request.method == 'POST':
        registration_form = CustomUserCreationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('')
        else:
            error(request, 'An error occurred during registration')

    context = {'form': registration_form}
    return render(request, 'registration_page.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('')



