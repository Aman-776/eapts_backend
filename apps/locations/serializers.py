from rest_framework import serializers
from .models import Location, LocationTag, LocationTagMap

class LocationTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationTag
        fields = '__all__'

class LocationTagMapSerializer(serializers.ModelSerializer):
    location_tag = serializers.PrimaryKeyRelatedField(queryset=LocationTag.objects.all())

    class Meta:
        model = LocationTagMap
        fields = ['location_tag']

class LocationSerializer(serializers.ModelSerializer):
    # Accept list of tag IDs during creation
    tags = LocationTagMapSerializer(many=True, write_only=True)

    class Meta:
        model = Location
        fields = ['id', 'name', 'parent', 'address', 'contact_info', 'tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        location = Location.objects.create(**validated_data)

        # Create the LocationTagMap objects
        for tag_data in tags_data:
            LocationTagMap.objects.create(location=location, location_tag=tag_data['location_tag'])

        return location

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)

        # Update basic fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update tags if provided
        if tags_data is not None:
            # Remove existing tag mappings
            LocationTagMap.objects.filter(location=instance).delete()
            # Add new ones
            for tag_data in tags_data:
                LocationTagMap.objects.create(location=instance, location_tag=tag_data['location_tag'])

        return instance
