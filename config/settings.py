import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.products',
    'apps.users',
    'apps.shopping_cart',
]

THIRD_APPS = [
    'tailwind',
    'theme',
    'django_browser_reload',
    'fontawesomefree',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': config('GOOGLE_CLIENT_ID'),
            'secret': config('GOOGLE_CLIENT_SECRET'),
            'key': '',
        }
    }
}

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = ["127.0.0.1"]

NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"

BASE_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

LOCAL_MIDDLEWARE = []

THIRD_MIDDLEWARE = [
    "allauth.account.middleware.AccountMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

MIDDLEWARE = BASE_MIDDLEWARE + LOCAL_MIDDLEWARE + THIRD_MIDDLEWARE

ROOT_URLCONF = 'config.urls'

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = 'users.Profiles'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

MEDIA_URL = "/media/"

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'templates/static',
]

STATIC_ROOT = 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGIN_URL = 'account_login'
LOGOUT_URL = 'account_logout'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'account_login'

# Configuración de allauth
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_URL_OVERLOAD = 'home'
# Configuración de las redirecciones de URLs de allauth
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_REDIRECT_URL
# Configuración de las redirecciones de URLs al cambiar la contraseña
ACCOUNT_CHANGE_PASSWORD_REDIRECT_URL = LOGIN_REDIRECT_URL
# Configuración de las plantillas de allauth con prefijo 'auth/'
ACCOUNT_TEMPLATE_PREFIX = 'account/'

# Configuración de la plantilla de correo electrónico para la confirmación de correo electrónico
# ACCOUNT_EMAIL_CONFIRMATION_SUBJECT = 'Confirma tu dirección de correo electrónico en Ecomer'
# ACCOUNT_EMAIL_CONFIRMATION_SUBJECT_TEMPLATE = 'account/email/confirmation_signup_subject.txt'
# ACCOUNT_EMAIL_CONFIRMATION_MESSAGE = 'account/email/confirmation_signup_message.txt'

# Configuración para permitir el inicio de sesión con la dirección de correo electrónico
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# # Configuración para personalizar las vistas de allauth
# ACCOUNT_ADAPTER = 'tu_app.adapter.CustomAccountAdapter'


# # Dirección de correo electrónico del servidor para enviar mensajes de error a los administradores
# SERVER_EMAIL = 'error@dominio.com'


# # Dirección de correo electrónico predeterminada para enviar notificaciones
# DEFAULT_FROM_EMAIL = 'tu_correo@dominio.com'

# Configuración del formulario de registro personalizado
ACCOUNT_FORMS = {'signup': 'apps.users.forms.CreateUsersForm'}
