from django.urls import path
from .views import landingPage

app_name = 'canwe'

urlpatterns = [
    path('', landingPage, name="landingPage"),
    path('canwe/', landingPage, name="landingPage")
]