from django.db import models as m


class WeatherModel(m.Model):
    date = m.DateTimeField(null=True, blank=True)
    maxdegree = m.TextField(null=True, blank=True)
    mindegree = m.TextField(null=True, blank=True)
