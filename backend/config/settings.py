from pathlib import Path
import os
from .logging import LOGGING

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-secret-key")
DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",")


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'rest_framework.authtoken',
    'oauth2_provider',

    "modules.usuarios",
    "modules.estaciones",
]

AUTH_USER_MODEL = "usuarios.UsuarioModel"

# Django REST Framework minimal config
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # "rest_framework.authentication.SessionAuthentication",
        # "rest_framework.authentication.TokenAuthentication",
        # "rest_framework.authentication.BasicAuthentication",
        "modules.auth0.infrastructure.authentication.Auth0JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "config.middleware.adminMiddleware.AdminPathMiddleware",

    # "modules.auth0.infrastructure.middleware.Auth0Middleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "bikeup"),
        "USER": os.getenv("POSTGRES_USER", "bikeuser"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "bikepass"),
        "HOST": os.getenv("POSTGRES_HOST", "postgresql"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_URL", "redis://redis:6379/0"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        "TIMEOUT": 3600,
    }
}


AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN", "dev-k7he8aiy4o7b4ba7.us.auth0.com")
AUTH0_CLIENT_ID3 = os.getenv("AUTH0_CLIENT_ID", "KRpKicS71EDI1YaeLQ0L0W7fcUugpG1G")
AUTH0_CLIENT_SECRET3 = os.getenv("AUTH0_CLIENT_SECRET", "KQNsQ275FEy6PhCDui5ZJ2JPdF4oBEHu6NxEtNHYG4wN6au3SwXczxXZiXM_84Ch")

AUTH0_CLIENT_ID4 = os.getenv("AUTH0_CLIENT_ID", "XsfLAPzjgkt8Jlx14512rV3XQweKEZ2B")
AUTH0_CLIENT_SECRET4 = os.getenv("AUTH0_CLIENT_SECRET", "WwS-KTvKO3pua68o3dgMQU3KfUQ1M4M_8jqbp68T5E57mQQA1O9B3HUsjy7fD55_")
AUTH0_API_AUDIENCE4 = os.getenv("AUTH0_AUDIENCE", "sda-test-id")


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "no-reply@bikeup.com"

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'tu_correo@gmail.com'
# EMAIL_HOST_PASSWORD = 'tu_contraseña_de_aplicacion'
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Internationalization
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = LOGGING