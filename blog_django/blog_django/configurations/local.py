from .base import *
import os  
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Configuraciones de base de datos de desarrollo
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Asegúrate de que esta ruta sea correcta
    }
}
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Asegúrate de que esta ruta sea correcta
]


os.environ['DJANGO_PORT'] = '8000'  # PUERTO PREDETERMINADO
