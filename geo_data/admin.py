from django.contrib import admin

# Register your models here.

from .models import Geo_data


class Geo_dataAdmin(admin.ModelAdmin):
    list_display = ["id", "latitude", "longitude",
                    "created_at", "updated_at", "user"]
    search_fields = ["id", "latitude", "longitude",
                     "created_at", "updated_at", "user__id"]


admin.site.register(Geo_data, Geo_dataAdmin)
