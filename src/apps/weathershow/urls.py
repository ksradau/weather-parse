from django.urls import path

from apps.weathershow.apps import WeatherConfig
from apps.weathershow.views import WeatherView

app_name = WeatherConfig.name

urlpatterns = [
    path("", WeatherView.as_view(), name="weathershow"),
]