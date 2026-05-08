from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # APIs
    path("api/locations/", include("apps.locations.urls")),
    path("api/person/", include("apps.person.urls")),
]
