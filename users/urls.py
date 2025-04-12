from django.urls import path
from users.views import DiscordLogin

urlpatterns = [
    # ... andere Routen ...
    path("api/auth/social/discord/", DiscordLogin.as_view(), name="discord_login"),
]
