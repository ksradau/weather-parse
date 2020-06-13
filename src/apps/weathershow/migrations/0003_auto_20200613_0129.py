# Generated by Django 3.0.7 on 2020-06-12 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weathershow', '0002_auto_20200612_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weathermodel',
            name='day',
        ),
        migrations.RemoveField(
            model_name='weathermodel',
            name='month',
        ),
        migrations.RemoveField(
            model_name='weathermodel',
            name='year',
        ),
        migrations.AddField(
            model_name='weathermodel',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]