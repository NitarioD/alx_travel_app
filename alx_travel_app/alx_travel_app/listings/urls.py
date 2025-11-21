# listings/urls.py
from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    # We'll add URL patterns here later
    # For now, just a simple placeholder
    path('', views.api_overview, name='api_overview'),
]