from django.db import models
import geocoder

# Create your models here.


class Data(models.Model):
    country = models.CharField(max_length=100, null=True)
    populations = models.PositiveIntegerField(null=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'Data'

    def save(self, *arg, **kwargs):
        self.latitude = geocoder.osm(self.country).lat
        self.longitude = geocoder.osm(self.country).lng
        return super().save(*arg, **kwargs)

    def __str__(self):
        return self.country

