from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv
import dj_database_url

# ------------------------------------------------------------
# 📁 Base Directory + .env Laden
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

# ------------------------------------------------------------
# 🔐 Security Settings
# ------------------------------------------------------------

try:
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
except KeyError:
    raise RuntimeError("DJANGO_SECRET_KEY environment variable is not set!")

DEBUG = os.environ.get("DJANGO_DEBUG", "") != "False"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "api.igoultra.de",  # ✅ production backend subdomain
    ".herokuapp.com",
]

# ------------------------------------------------------------
# 📦 Installed Applications
# ------------------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third-party apps
    'corsheaders',
    'django_extensions',
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

# ------------------------------------------------------------
# 👤 User Model and Site ID
# ------------------------------------------------------------

AUTH_USER_MODEL = 'users.CustomUser'
SITE_ID = 2

# ------------------------------------------------------------
# 🔑 REST Framework + Session Auth (No JWT)
# ------------------------------------------------------------

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}

REST_USE_JWT = False  # Sessions only

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_UNIQUE_EMAIL = True

# ------------------------------------------------------------
# 🔐 Discord OAuth2 Settings
# ------------------------------------------------------------

SOCIALACCOUNT_PROVIDERS = {
    'discord': {
        'SCOPE': ['identify', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'OAUTH_PKCE_ENABLED': True,
    }
}

# ✅ Redirect-URLs über Umgebungsvariablen steuerbar
LOGIN_REDIRECT_URL = os.getenv("LOGIN_REDIRECT_URL", "/accounts/profile/")
ACCOUNT_LOGOUT_REDIRECT_URL = os.getenv("ACCOUNT_LOGOUT_REDIRECT_URL", "/")

ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"
SOCIALACCOUNT_ADAPTER = "allauth.socialaccount.adapter.DefaultSocialAccountAdapter"

# ------------------------------------------------------------
# 🧱 Middleware
# ------------------------------------------------------------

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------------------------------------------------
# 🖼 Templates
# ------------------------------------------------------------

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

# ------------------------------------------------------------
# 💾 Database
# ------------------------------------------------------------

DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}'
    )
}

# ------------------------------------------------------------
# 🔐 Password Validators
# ------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------------------------------------
# 🌐 Internationalization
# ------------------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------------------------------------
# 🎨 Static Files (for Heroku deployment)
# ------------------------------------------------------------

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ------------------------------------------------------------
# 🌐 CORS Configuration
# ------------------------------------------------------------

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:3000",           # ✅ Local React app
    "https://app.igoultra.de",         # ✅ Vercel frontend
]

CORS_ALLOW_CREDENTIALS = True

# ------------------------------------------------------------
# 🍪 Secure Cookie Settings (for Cross-Origin Cookies)
# ------------------------------------------------------------

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "None"  # Required for cross-site cookies

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "None"

# ------------------------------------------------------------
# 📧 Email Configuration (Dev only)
# ------------------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
