
from django.db import models
from django.conf import settings


class Geo_data(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return f"on {self.updated_at} {self.user} location = {self.latitude} , {self.longitude}"
        return f"geo_data is {self.latitude} , {self.longitude}"
