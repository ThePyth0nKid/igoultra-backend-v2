from django.db import models
from django.conf import settings

class SeasonScore(models.Model):
    MODE_CHOICES = (
        ("reality", "Reality"),
        ("cyber", "Cyber")
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    season = models.DateField()  # e.g. 2025-04-01
    mode = models.CharField(
        max_length=10,
        choices=MODE_CHOICES
    )
    xp = models.IntegerField(default=0)
    layer = models.CharField(max_length=10, default="RL1")
    position = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} – {self.mode.upper()} {self.season}"
