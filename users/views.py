# users/views.py

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.discord.views import DiscordOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.utils.decorators import method_decorator

# Import your custom user serializer
from .serializers import UserSerializer


# 🔐 Discord OAuth2 Login View
class DiscordLogin(SocialLoginView):
    adapter_class = DiscordOAuth2Adapter
    callback_url = "http://localhost:5173/discord/callback"  # Update for production!
    client_class = OAuth2Client


# 👤 Returns the current authenticated user info
class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


# 🍪 Ensures a CSRF token is set in the cookie for session-based requests (needed for logout)
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"detail": "CSRF cookie set."})
