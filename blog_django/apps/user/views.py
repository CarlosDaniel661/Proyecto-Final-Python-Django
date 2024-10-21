# blog_django/apps/user/views.py

from django.views.generic import TemplateView, CreateView, DetailView
from django.contrib.auth.views import LoginView as LoginViewDjango, LogoutView as LogoutViewDjango
from apps.user.forms import RegisterForm, LoginForm
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from apps.user.models import User
from django.shortcuts import get_object_or_404, render

# Vista para la página "Nosotros"
def nosotros(request):
    return render(request, 'user/nosotros.html')

# Vista para "Avisos Legales"
def avisos_legales(request):
    return render(request, 'user/avisos_legales.html')

# Vista para "Políticas de Privacidad"
def politic_privacidad(request):
    return render(request, 'user/politic_privacidad.html')

class UserProfileView(DetailView):
    model = User
    template_name = 'user/user_profile.html'
    context_object_name = 'user'  # Usa este atributo en lugar de modificar el contexto manualmente

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs['pk'])

class RegisterView(CreateView):
    template_name = 'auth/auth_register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('user:auth_login')  # Redirige al login después del registro
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Asignar el grupo 'Registered' al usuario recién creado
        try:
            registered_group = Group.objects.get(name='Registered')
            self.object.groups.add(registered_group)
        except Group.DoesNotExist:
            pass  # Maneja el caso en que el grupo no exista (o crea el grupo si lo prefieres)
        
        return response

class LoginView(LoginViewDjango):
    template_name = 'auth/auth_login.html'
    authentication_form = LoginForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('home')  # Redirige al home una vez logueado

class LogoutView(LogoutViewDjango):
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('home')  # Redirige al home después de cerrar sesión
    
class IndexView(TemplateView):
    template_name = 'user/index.html'
