from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom user model with optional Discord ID field
class CustomUser(AbstractUser):
    discord_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
