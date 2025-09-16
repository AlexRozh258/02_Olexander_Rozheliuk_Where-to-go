from django.db import models
from django.utils import timezone

class Place(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    place_type = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=200, blank=True)
    rating = models.PositiveSmallIntegerField(default=3)
    created_at = models.DateTimeField(default=timezone.now)

    def short_description(self, n=20):
        return ' '.join(self.description.split()[:n])

    def __str__(self):
        return self.title
