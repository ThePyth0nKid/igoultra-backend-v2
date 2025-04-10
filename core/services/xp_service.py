from xp.models import UserProfile
from core.constants.levels import get_level_for_xp

# Add XP and update level
def add_xp_to_user(user, xp_amount):
    profile, _ = UserProfile.objects.get_or_create(user=user)
    profile.xp += xp_amount
    profile.level = get_level_for_xp(profile.xp)
    profile.save()
