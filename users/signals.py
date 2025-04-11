from allauth.socialaccount.signals import social_account_added
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(social_account_added)
def update_discord_id(sender, request, sociallogin, **kwargs):
    user = sociallogin.user
    if sociallogin.account.provider == 'discord':
        discord_id = sociallogin.account.uid  # Discord User ID
        user.discord_id = discord_id
        user.save()
