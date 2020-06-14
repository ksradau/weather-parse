from django.views.generic import ListView
import requests
from lxml import html
import datetime
from datetime import datetime
from datetime import timedelta
import pytz
from apps.weathershow.models import WeatherModel
import re



class WeatherView(ListView):
    template_name = "weathershow/index.html"
    model = WeatherModel


    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        w = WeatherModel.objects.get(id=1)
        d = w.date
        dnow = datetime.now().replace(tzinfo=pytz.utc) + timedelta(hours=3)   #plus 3 hours for Heroku

        delta = dnow - d

        if delta > timedelta(minutes=10):
            url = "https://www.gismeteo.by/weather-minsk-4248/"

            r = requests.get(url, headers={
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"})

            page = html.fromstring(r.text)

            max = str(page.xpath("/html/body/section/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[3]/div/div/div/div[2]/span[1]/text()"))
            min = str(page.xpath("/html/body/section/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[3]/div/div/div/div[1]/span[1]/text()"))
            current = str(page.xpath("/html/body/section/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/a[1]/div/div[1]/div[3]/div[1]/span[1]/span/text()"))
            feel = str(page.xpath("/html/body/section/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/a[1]/div/div[1]/div[3]/div[2]/span/span[1]/text()"))

            def clean_data(str):
                return '+' + ''.join([a for a in str if a.isdigit()])

            max_temp = clean_data(max)
            min_temp = clean_data(min)
            current_temp = clean_data(current)
            feel_temp = clean_data(feel)

            w = WeatherModel(
                id=1,
                date=dnow,
                maxdegree=max_temp,
                mindegree=min_temp,
                currentdegree=current_temp,
                feeldegree=feel_temp
            )
            w.save()

        ctx["weather"] = WeatherModel.objects.all()

        return ctx



