"""
Django settings for ultrabackend project.

Generated by 'django-admin startproject' using Django 5.2.
"""

from pathlib import Path
from datetime import timedelta

# ----------------------------------------------------------------
# 📁 Base Directory
# ----------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------------------------------------------
# 🔐 Security Settings
# ----------------------------------------------------------------

SECRET_KEY = 'django-insecure-vn4iu7ns787!46e@#^5=57_7&@tt2*)pgo+sn3mnl8ryk=)huj'
DEBUG = True
ALLOWED_HOSTS = []

# ----------------------------------------------------------------
# 🧩 Installed Apps
# ----------------------------------------------------------------

INSTALLED_APPS = [
    # Default Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Auth system
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.discord',

    # Custom apps
    'users',
    'xp',
    'seasons',
]

# ----------------------------------------------------------------
# 🔐 User & Site Config
# ----------------------------------------------------------------

AUTH_USER_MODEL = 'users.CustomUser'
SITE_ID = 1

# ----------------------------------------------------------------
# 🔐 REST Framework & Auth Config
# ----------------------------------------------------------------

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# JWT Settings for dj-rest-auth
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

# Allauth settings
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_UNIQUE_EMAIL = True

# Discord OAuth Settings
SOCIALACCOUNT_PROVIDERS = {
    'discord': {
        'SCOPE': ['identify', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'OAUTH_PKCE_ENABLED': True
    }
}

# ----------------------------------------------------------------
# 🔧 Middleware
# ----------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------------------------------------------------------
# 📦 Templates
# ----------------------------------------------------------------

ROOT_URLCONF = 'ultrabackend.urls'

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

WSGI_APPLICATION = 'ultrabackend.wsgi.application'

# ----------------------------------------------------------------
# 🗄️ Database
# ----------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ----------------------------------------------------------------
# 🔐 Password Validators
# ----------------------------------------------------------------

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

# ----------------------------------------------------------------
# 🌍 Localization
# ----------------------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ----------------------------------------------------------------
# 🎨 Static Files
# ----------------------------------------------------------------

STATIC_URL = 'static/'

# ----------------------------------------------------------------
# 🧠 Defaults
# ----------------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
