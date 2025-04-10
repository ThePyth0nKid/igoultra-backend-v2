from django.contrib import admin
from .models import UserProfile

# Register UserProfile for admin access
admin.site.register(UserProfile)