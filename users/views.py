# users/views.py

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.discord.views import DiscordOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Import the custom user serializer (make sure it exists in users/serializers.py)
from .serializers import UserSerializer

# 🔐 Discord OAuth2 Login View
# This class handles the OAuth2 login redirect flow via Discord
class DiscordLogin(SocialLoginView):
    adapter_class = DiscordOAuth2Adapter
    callback_url = "http://localhost:5173/discord/callback"  # Change this in production
    client_class = OAuth2Client

# 👤 Authenticated User Info View
# Returns the currently logged-in user's data (used on frontend for profile, etc.)
class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
