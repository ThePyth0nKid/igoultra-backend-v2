from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # REST Auth URLs (Login, Logout, Password Reset, etc.)
    path('api/auth/', include('dj_rest_auth.urls')),

    # Registration (optional, falls du neue User anlegen willst)
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),

    # Social Login (Discord etc.)
    path('api/auth/social/', include('allauth.socialaccount.urls')),
]
