from django.urls import path
from . import views

urlpatterns = [
    # Returns the logged-in user data
    path("", views.CurrentUserView.as_view(), name="current-user"),
]
