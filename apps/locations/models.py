from django.db import models

class LocationTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    address = models.TextField(blank=True)
    contact_info = models.TextField(blank=True)

    def __str__(self):
        return self.name


class LocationTagMap(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='tags')
    location_tag = models.ForeignKey(LocationTag, on_delete=models.CASCADE, related_name='locations')

    class Meta:
        unique_together = ('location', 'location_tag')

    def __str__(self):
        return f"{self.location.name} - {self.location_tag.name}"
