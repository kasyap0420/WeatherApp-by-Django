from django.db import models

# Create your models here.
from django.db import models

class Forecast(models.Model):
    city          = models.CharField(max_length=64)
    date          = models.DateField()
    temperature_c = models.IntegerField()
    condition     = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} on {self.date}: {self.temperature_c}°C, {self.condition}"
