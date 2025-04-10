# xp/models.py

from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    """
    Represents a user profile that extends the default user model.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the user model.
        xp (IntegerField): The experience points of the user, default is 0.
        level (IntegerField): The level of the user, default is 1.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    def __str__(self):
        """
        Returns a string representation of the UserProfile instance.

        Returns:
            str: The username of the user followed by ' Profile'.
        """
        return f'{self.user.username} Profile'
        return f'{self.user.username} Profile'
