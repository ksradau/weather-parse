from django.views.generic import FormView
from django.http import HttpResponse
import requests
from lxml import html
import datetime
from delorean import Delorean
from datetime import datetime
from datetime import timezone
from datetime import timedelta
import pytz
from apps.weathershow.forms import WeatherForm
from apps.weathershow.models import WeatherModel


w = WeatherModel.objects.get(id=1)
d = w.date
dnow = datetime.now().replace(tzinfo=pytz.utc)

delta = dnow - d

if delta > timedelta(minutes=30):
    url = "https://www.gismeteo.by/weather-minsk-4248/"

    r = requests.get(url, headers={
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"})

    page = html.fromstring(r.text)

    w = WeatherModel(
            id=1,
            date=dnow,
            maxdegree=str(page.xpath(
                "/html/body/section/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[3]/div/div/div/div[2]/span[1]/text()")),
            mindegree=str(page.xpath(
                "/html/body/section/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[3]/div/div/div/div[1]/span[1]/text()"))
        )
    w.save()


class WeatherView(FormView):
    template_name = "weathershow/index.html"
    form_class = WeatherForm
    success_url = ''

    http_method_names = ["get"]


    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)


        #weather.refresh_from_db()


        #self.object.date = datenow
        #self.object.maxdegree = max
        #self.object.mindegree = min
        #self.object.save()
        #self.object.refresh_from_db()

        # TODO:

        return ctx



