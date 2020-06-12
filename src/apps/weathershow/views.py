from django.views.generic import ListView

from apps.weathershow.models import WeatherModel
import requests
from lxml import html
import datetime


class WeatherView(ListView):
    template_name = "weathershow/index.html"
    model = WeatherModel

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        url = "https://www.gismeteo.by/weather-minsk-4248/"
        r = requests.get(url, headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"})
        page = html.fromstring(r.text)
        maxdegree = page.xpath("/html/body/section/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[3]/div/div/div/div[2]/span[1]/text()")
        mindegree = page.xpath("/html/body/section/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[3]/div/div/div/div[1]/span[1]/text()")

        now = datetime.datetime.now()

        weather = WeatherModel(day=now.day, month=now.month, year=now.year, maxdegree=maxdegree, mindegree=mindegree)
        weather.save()

        # TODO:

        return ctx