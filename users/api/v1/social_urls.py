from django.urls import path
from . import views

urlpatterns = [
    # Handles Discord OAuth2 login (called from frontend)
    path("discord/", views.discord_login_view, name="discord-login"),

    # Optional: Separate callback route, if needed
    path("callback/", views.discord_callback_view, name="discord-callback"),
]
