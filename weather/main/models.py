from django.db import models

# Create your models here.
class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    country_code = models.CharField(max_length=100)
    coordinate = models.CharField(max_length=100)
    temp = models.CharField(max_length=100)
    pressure = models.CharField(max_length=100)
    humidity = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)