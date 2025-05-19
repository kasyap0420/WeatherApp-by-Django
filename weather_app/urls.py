from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forecasts.urls')),
    path('api/', include('todo.urls')),  # ← add this line
]
