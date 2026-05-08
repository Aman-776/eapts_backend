from rest_framework import generics
from .models import Location, LocationTag, LocationTagMap
from .serializers import LocationSerializer, LocationTagSerializer, LocationTagMapSerializer

# --------------------
# Location Views
# --------------------
class LocationListCreate(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


# --------------------
# LocationTag Views
# --------------------
class LocationTagListCreate(generics.ListCreateAPIView):
    queryset = LocationTag.objects.all()
    serializer_class = LocationTagSerializer


class LocationTagRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = LocationTag.objects.all()
    serializer_class = LocationTagSerializer


# --------------------
# LocationTagMap Views
# --------------------
class LocationTagMapListCreate(generics.ListCreateAPIView):
    queryset = LocationTagMap.objects.all()
    serializer_class = LocationTagMapSerializer


class LocationTagMapRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = LocationTagMap.objects.all()
    serializer_class = LocationTagMapSerializer
