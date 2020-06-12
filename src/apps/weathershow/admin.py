from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.weathershow.models import WeatherModel


@admin.register(WeatherModel)
class WeatherAdminModel(ModelAdmin):
    pass