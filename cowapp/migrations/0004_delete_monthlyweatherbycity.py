# Generated by Django 2.0.7 on 2018-08-12 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cowapp', '0003_monthlyweatherbycity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MonthlyWeatherByCity',
        ),
    ]
