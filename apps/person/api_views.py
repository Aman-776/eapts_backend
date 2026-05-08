from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from locations.models import Location, LocationTagMap
from .serializers import LocationSerializer

@api_view(['GET'])
def locations_list(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')
    location_id = request.data.get('location_id')

    if not all([username, password, location_id]):
        return Response({"error": "All fields required"}, status=400)

    user = authenticate(request, username=username, password=password)
    if user is None:
        return Response({"error": "Invalid credentials"}, status=401)

    # Login user
    login(request, user)

    try:
        location = Location.objects.get(id=location_id)
        tagmap = LocationTagMap.objects.filter(location=location).first()
        location_tag = tagmap.location_tag.name if tagmap else None
    except Location.DoesNotExist:
        return Response({"error": "Invalid location"}, status=400)

    # Save in session if needed
    request.session['location_id'] = location.id
    request.session['location_name'] = location.name
    request.session['location_tag'] = location_tag

    return Response({
        "username": user.username,
        "location_name": location.name,
        "location_tag": location_tag
    })
