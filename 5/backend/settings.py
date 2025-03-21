"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3+bq_p5&pfckn=xd9mw&s=p%g^ugv@3^=*$@b(@hqz=32z!qpb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
LOG = True

ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:3000",
# ]
#
# CSRF_TRUSTED_ORIGINS = [
#     "http://127.0.0.1:3000",
# ]

# Application definition

INSTALLED_APPS = [
    'grappelli',
    "corsheaders",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'api',

    'rest_framework',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'frontend'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
POSTGRES = False
if POSTGRES:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'example',
            'USER': 'postgres',
            'PASSWORD': '31284bogdan',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Etc/GMT-6'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

if DEBUG:
    STATIC_URL = '/static/'
    # STATIC_ROOT = Path(BASE_DIR / 'static')
    STATIC_DIR = Path(BASE_DIR / 'static')
    STATICFILES_DIRS = [
        Path(BASE_DIR / 'static_external'),
        Path(BASE_DIR / 'static'),
        Path(BASE_DIR / 'frontend/build/static'),
        Path(BASE_DIR / 'frontend/public/static'),
    ]
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = Path(BASE_DIR / 'static')
    STATIC_DIR = Path(BASE_DIR / 'static')
    STATICFILES_DIRS = [
        Path(BASE_DIR / 'static_external'),
        # Path(BASE_DIR / 'static'),
        Path(BASE_DIR / 'frontend/build/static'),
        Path(BASE_DIR / 'frontend/public/static'),
    ]

MEDIA_URL = '/media/'
MEDIA_ROOT = Path(BASE_DIR, 'static/media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

FROM_EMAIL = 'eevee.cycle1@yandex.ru'
EMAIL_ADMIN = 'eevee.cycle1@yandex.ru'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "eevee.cycle1@yandex.ru"
EMAIL_HOST_PASSWORD = "31284Bogdan"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

host: EMAIL_HOST
port: EMAIL_PORT
username: EMAIL_HOST_USER
password: EMAIL_HOST_PASSWORD
use_tls: EMAIL_USE_TLS
use_ssl: EMAIL_USE_SSL
