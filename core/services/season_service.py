from core.utils.time import get_current_season
from seasons.models import SeasonScore

def add_season_xp(user, amount, mode):
    season = get_current_season()
    score, _ = SeasonScore.objects.get_or_create(
        user=user,
        season=season,
        mode=mode
    )
    score.xp += amount
    score.save()
