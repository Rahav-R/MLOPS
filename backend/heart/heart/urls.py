# heart/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('predictor/', include('predictor.urls')),  # Include the predictor app URLs for /predictor/
    path('', include('predictor.urls')),  # Set the root URL (/) to go to the predictor's home
]
