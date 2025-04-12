import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


@api_view(['POST'])
def discord_login_view(request):
    """
    Handles the OAuth2 code returned from Discord and forwards it
    to allauth's internal callback to finalize the login.
    Returns debug info if something fails.
    """
    code = request.data.get("code")

    if not code:
        return Response({"error": "No code provided."}, status=status.HTTP_400_BAD_REQUEST)

    # Construct the full callback URL
    callback_url = f"{settings.BASE_URL}/accounts/discord/login/callback/?code={code}"

    try:
        # Create a session to forward cookies if needed
        session = requests.Session()

        # Don't follow redirects – we want to inspect the raw response
        response = session.get(
            callback_url,
            cookies=request.COOKIES,
            allow_redirects=False,
            timeout=10
        )

        # If redirect to frontend or success page
        if response.status_code == 302:
            return Response({"success": True, "redirect_to": response.headers.get("Location")})

        # Unexpected status – show debug info
        return Response({
            "error": "Login failed or unexpected response.",
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "text": response.text[:500],  # limit response text
        }, status=status.HTTP_400_BAD_REQUEST)

    except requests.RequestException as e:
        # Network or connection error
        return Response({"error": f"Request failed: {str(e)}"}, status=status.HTTP_502_BAD_GATEWAY)

    except Exception as e:
        # Any other internal error
        return Response({"error": f"Internal error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CurrentUserView(APIView):
    """
    Returns the currently logged-in user's data.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
        })


@api_view(['GET'])
def discord_callback_view(request):
    """
    Optional debug view for Discord callback (rarely needed).
    """
    return Response({"message": "Callback reached"})
