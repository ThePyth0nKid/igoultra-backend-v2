from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin Panel
    path('admin/', admin.site.urls),

    # 🔐 API Auth (Login, Logout, Password Reset, Token Auth, etc.)
    path('api/auth/', include('dj_rest_auth.urls')),

    # 📝 Registration (normal email/username-based registration)
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),

    # 🌐 Social Login API (z. B. für Discord, Google, etc.)
    path('api/auth/social/', include('allauth.socialaccount.urls')),

    # 🔁 Allauth für Social OAuth-Redirects (z. B. Discord-Login: /accounts/discord/login/)
    path('accounts/', include('allauth.urls')),
]
