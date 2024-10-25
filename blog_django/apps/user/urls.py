# blog_django/apps/user/urls.py
from django.urls import path
from apps.user import views

app_name = 'user'

urlpatterns = [
    path('profile/', views.user_profile_view, name="profile"),  # Vista de perfil del usuario
    path('auth/register/', views.RegisterView.as_view(), name="auth_register"),  # Registro
    path('auth/login/', views.LoginView.as_view(), name="auth_login"),  # Login
    path('auth/logout/', views.LogoutView.as_view(), name="auth_logout"),  # Logout
    path('', views.IndexView.as_view(), name='home'),  # Página principal
    path('nosotros/', views.nosotros, name='nosotros'),
    path('avisos_legales/', views.avisos_legales, name='avisos_legales'),
    path('politc_privacidad/', views.politc_privacidad, name='politc_privacidad'),
]
