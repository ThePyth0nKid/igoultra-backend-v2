from django.urls import path
from .views import DiscordLogin, CurrentUserView
from dj_rest_auth.views import LogoutView

urlpatterns = [
    # 🌐 Discord Social Login Endpoint
    path("discord/", DiscordLogin.as_view(), name="discord_login"),

    # 👤 Aktueller eingeloggter User (für Navbar, Dashboard etc.)
    path("me/", CurrentUserView.as_view(), name="current_user"),

    # 🚪 Optional: Logout über Session
    path("logout/", LogoutView.as_view(), name="rest_logout"),
]
