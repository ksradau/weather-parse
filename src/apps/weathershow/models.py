from django.db import models as m


class WeatherModel(m.Model):
    day = m.IntegerField(null=True, blank=True)
    month = m.IntegerField(null=True, blank=True)
    year = m.IntegerField(null=True, blank=True)
    maxdegree = m.TextField(null=True, blank=True)
    mindegree = m.TextField(null=True, blank=True)
