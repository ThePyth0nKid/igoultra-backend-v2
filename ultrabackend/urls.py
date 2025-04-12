from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin Panel
    path("admin/", admin.site.urls),

    # 🌐 Discord Login only
    path("api/auth/discord/", include("users.urls")),  # /api/auth/discord/

    # 🔁 Allauth redirect handler (OAuth-Flow via /accounts/)
    path("accounts/", include("allauth.urls")),
    
    # 🧑 User Info API (e.g. /api/users/me/)
    path("api/users/", include("users.urls")),
]
