from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # API Auth (Login, Logout, Token, etc.)
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),

    # Social login API (falls du später eigene Views hast)
    path('api/auth/social/', include('allauth.socialaccount.urls')),

    # ⚠️ Wichtig für den Discord-Redirect-Login über /accounts/...
    path('accounts/', include('allauth.urls')),
]
