from django.urls import path
from .views import (
    DiscordLogin,
    CurrentUserView,
    get_csrf_token,
)
from dj_rest_auth.views import LogoutView

urlpatterns = [
    # 🌐 Discord OAuth2 Login
    # POST /api/v1/auth/discord/  (Discord Code → Session wird erstellt)
    path("discord/", DiscordLogin.as_view(), name="discord_login"),

    # 👤 Current User Info
    # GET /api/v1/auth/me/  (Gibt eingeloggten User zurück – für Navbar, Dashboard etc.)
    path("me/", CurrentUserView.as_view(), name="current_user"),

    # 🚪 Logout
    # POST /api/v1/auth/logout/  (Session wird beendet, CSRF nötig)
    path("logout/", LogoutView.as_view(), name="rest_logout"),

    # 🍪 CSRF Token holen
    # GET /api/v1/auth/csrf/  (Nur um CSRF-Cookie zu setzen für sichere POSTs)
    path("csrf/", get_csrf_token, name="get_csrf_token"),
]
