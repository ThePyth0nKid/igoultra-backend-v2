from django.urls import path
from .views import DiscordLogin, CurrentUserView
from dj_rest_auth.views import LogoutView

urlpatterns = [
    # 🌐 Discord OAuth2 Social Login
    # This handles the login redirect via the frontend -> Discord -> backend
    path("discord/", DiscordLogin.as_view(), name="discord_login"),

    # 👤 Fetch current logged-in user info (for profile, navbar, dashboard, etc.)
    path("me/", CurrentUserView.as_view(), name="current_user"),

    # 🚪 Logout endpoint (works with session-based login like Discord OAuth)
    path("logout/", LogoutView.as_view(), name="rest_logout"),
]
