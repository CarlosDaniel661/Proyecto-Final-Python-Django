from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog_django.views import IndexView, not_found_view, internal_error_view, forbidden_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Ruta del administrador
    path('admin/', admin.site.urls),
    
    # Página de inicio
    path('', IndexView.as_view(), name='home'),

    # Incluyendo las rutas de la app 'user'
    path('user/', include('apps.user.urls')),

    # Incluyendo las rutas de la app 'post'
    path('posts/', include('apps.post.urls')),

    # Autenticación de usuarios
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

# Manejadores de errores
handler404 = not_found_view
handler500 = internal_error_view
handler403 = forbidden_view

# Sirviendo archivos estáticos y media si estás en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
