from django.urls import path
from apps.user import views

app_name = 'user'

urlpatterns = [
    path('users/profile/<uuid:pk>/', views.UserProfileView.as_view(), name="user_profile"),  # Cambiado a int si es un entero
    path('auth/register/', views.RegisterView.as_view(), name="auth_register"),  # Registro
    path('auth/login/', views.LoginView.as_view(), name="auth_login"),  # Login
    path('auth/logout/', views.LogoutView.as_view(), name="auth_logout"),  # Logout
    path('', views.IndexView.as_view(), name='home'),  # Página principal
    path('nosotros/', views.nosotros, name='nosotros'),
    path('avisos_legales/', views.avisos_legales, name='avisos_legales'),
    path('politic_privacidad/', views.politic_privacidad, name='politic_privacidad'),
]
