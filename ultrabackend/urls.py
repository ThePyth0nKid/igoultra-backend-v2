from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Main API namespace (v1)
    path("api/v1/", include("api.v1.urls")),

    # Required for allauth to handle OAuth2 redirects
    path("accounts/", include("allauth.urls")),
]
