from django.contrib import admin
from .models import Forecast

@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ("city", "date", "temperature_c", "condition")
