# person/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from apps.locations.models import Location, LocationTagMap
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.contrib.auth import logout

@api_view(['POST'])
def login_api(request):
    username = request.data.get("username")
    password = request.data.get("password")
    location_id = request.data.get("location_id")

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({"error": "Invalid credentials"}, status=400)

    login(request, user)

    try:
        location = Location.objects.get(id=location_id)
        tagmap = LocationTagMap.objects.filter(location=location).first()
        location_tag = tagmap.location_tag.name if tagmap else None
    except Location.DoesNotExist:
        return Response({"error": "Invalid location"}, status=400)

    return Response({"location_tag": location_tag})

@api_view(['POST'])
def logout_api(request):
    logout(request)  # This clears the session
    return Response({"success": "Logged out"})

@ensure_csrf_cookie
def get_csrf(request):
    return JsonResponse({"detail": "CSRF cookie set"})