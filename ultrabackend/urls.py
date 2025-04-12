# ultrabackend/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # dj-rest-auth default endpoints (login, password reset, etc.)
    path("api/auth/", include("dj_rest_auth.urls")),

    # Social Login (custom routes like /api/auth/social/discord/)
    path("api/auth/social/", include("users.urls")),  # 👈 this line is key

    # Optional: Allauth default URLs (needed for Discord redirect flow)
    path("accounts/", include("allauth.urls")),
]
