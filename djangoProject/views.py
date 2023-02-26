from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserLoginForm
from django.contrib.messages import error, warning, success
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.views import View
from django.contrib.auth.decorators import login_required
from djangoProject.models import User


class IndexView(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context=context)


def registration_page_view(request):
    if request.method == 'GET':
        registration_form = CustomUserCreationForm()
        context = {'form': registration_form}
        return render(request, 'registration_page.html', context=context)

    if request.method == 'POST':
        registration_form = CustomUserCreationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save(commit=True)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            success(request, 'You have registered successfully')
            return redirect('main_page')
        else:
            context = {'form': registration_form}
            return render(request, 'registration_page.html', context=context)


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    # authentication_form =
    template_name = 'login_page.html'

    def get_success_url(self):
        return redirect('main_page')

    def form_invalid(self, form):
        error(self.request, 'Login form is invalid')
        return self.render_to_response(self.get_context_data(form=form))


class CustomLogoutView(LogoutView):
    pass


class CustomPasswordResetView(PasswordResetView):
    pass
