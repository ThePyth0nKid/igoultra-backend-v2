from django.urls import path, include

urlpatterns = [
    # Discord login system
    path("auth/social/", include("users.api.v1.social_urls")),

    # User profile (logged-in user info)
    path("user/", include("users.api.v1.profile_urls")),
]
