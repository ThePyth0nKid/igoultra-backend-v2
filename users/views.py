from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.discord.views import DiscordOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

from .serializers import UserSerializer


# 🔐 Discord OAuth2 Login via dj-rest-auth SocialLoginView (API-style)
class DiscordLogin(SocialLoginView):
    adapter_class = DiscordOAuth2Adapter
    callback_url = "http://localhost:5173/discord/callback"  # Update in production!
    client_class = OAuth2Client


# 👤 Returns the current authenticated user's data (requires session cookie)
class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


# 🍪 Ensures CSRF token is sent in cookie (needed for safe logout & POST)
@ensure_csrf_cookie
@api_view(["GET"])
@permission_classes([])
def get_csrf_token(request):
    return JsonResponse({"detail": "CSRF cookie set."})


# 🔓 Optional: Logout endpoint using session & CSRF protection
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return Response({"detail": "Logged out successfully."})
