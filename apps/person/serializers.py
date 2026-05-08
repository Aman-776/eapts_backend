from rest_framework import serializers
from locations.models import Location, LocationTagMap

class LocationSerializer(serializers.ModelSerializer):
    tag_name = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ['id', 'name', 'tag_name']

    def get_tag_name(self, obj):
        tagmap = LocationTagMap.objects.filter(location=obj).first()
        return tagmap.location_tag.name if tagmap else None
