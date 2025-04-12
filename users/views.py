from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.discord.views import DiscordOAuth2Adapter

class DiscordLogin(SocialLoginView):
    adapter_class = DiscordOAuth2Adapter
