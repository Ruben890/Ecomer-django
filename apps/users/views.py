from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from .forms import LoginForm, CreateUsersForm
from django.contrib.auth import login

# ? Auth AUTHENTICATION
# * Vista para el inicio de sesión
class Login(LoginView):
    template_name = 'page/auth/login.html'
    fields = '__all__'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

# *Vista para el registro de usuario


class Register(FormView):
    fields = '__all__'
    template_name = 'page/auth/register.html'
    form_class = CreateUsersForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')  # Corrected redirection
        return super(Register, self).get(*args, **kwargs)