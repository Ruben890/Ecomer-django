from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from .forms import LoginForm, CreateUsersForm
from django.contrib.auth import login

# Vista para el inicio de sesión
class CustomLoginView(LoginView):
    template_name = 'page/auth/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

# Vista para el registro de usuario
class CreateUsersView(View):
    template_name = 'page/auth/register.html'

    def get(self, request):
        form = CreateUsersForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreateUsersForm(request.POST, request.FILES)
        if form.is_valid():
            user = self.process_valid_form(form)
            if user:
                self.login_user(request, user)
                return redirect('home')
        return render(request, self.template_name, {'form': form})

    def process_valid_form(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.set_password(form.cleaned_data['password'])
        user.save()
        return user

    def login_user(self, request, user):
        login(request, user)
