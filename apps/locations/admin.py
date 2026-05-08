from django.contrib import admin
from .models import Location, LocationTag, LocationTagMap

admin.site.register(Location)
admin.site.register(LocationTag)
admin.site.register(LocationTagMap)
