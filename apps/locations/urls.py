from django.urls import path
from .views import (
    LocationListCreate, LocationRetrieveUpdateDelete,
    LocationTagListCreate, LocationTagRetrieveUpdateDelete,
    LocationTagMapListCreate, LocationTagMapRetrieveUpdateDelete,
)

urlpatterns = [
    # Locations
    path("", LocationListCreate.as_view(), name="locations_list_create"),
    path("<int:pk>/", LocationRetrieveUpdateDelete.as_view(), name="location_rud"),

    # Location Tags
    path("tags/", LocationTagListCreate.as_view(), name="location_tags_list_create"),
    path("tags/<int:pk>/", LocationTagRetrieveUpdateDelete.as_view(), name="location_tag_rud"),

    # Location Tag Maps
    path("maps/", LocationTagMapListCreate.as_view(), name="location_tag_maps_list_create"),
    path("maps/<int:pk>/", LocationTagMapRetrieveUpdateDelete.as_view(), name="location_tag_map_rud"),
]
