from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, blank=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __str__(self):
        return self.name
