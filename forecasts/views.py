import os
import requests
from django.shortcuts import render
from .models import Forecast

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def home(request):
    city = request.GET.get("city", "Guntur")
    resp = requests.get(BASE_URL, params={
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    })
    data = resp.json()

    context = {}
    if resp.status_code == 200:
        context["weather"] = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "desc": data["weather"][0]["description"].title(),
        }
    else:
        context["error"] = data.get("message", "Could not fetch weather.")

    context["forecasts"] = Forecast.objects.all().order_by("-date")[:5]
    return render(request, "forecasts/home.html", context)
