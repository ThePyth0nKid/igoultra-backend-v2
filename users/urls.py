from django.urls import path
from .views import DiscordLogin

urlpatterns = [
    path("discord/", DiscordLogin.as_view(), name="discord_login"),
]
