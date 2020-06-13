from django import forms

from apps.weathershow.models import WeatherModel


def a(obj):
    return obj.field.name


class WeatherForm(forms.ModelForm):
    class Meta:
        model = WeatherModel

        widgets = {
            a(WeatherModel.date): forms.HiddenInput,
            a(WeatherModel.mindegree): forms.HiddenInput,
            a(WeatherModel.maxdegree): forms.HiddenInput,
        }


        fields = [a(_f) for _f in (WeatherModel.date, WeatherModel.mindegree, WeatherModel.maxdegree,)]
