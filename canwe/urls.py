from django.urls import path
from .views import index

app_name = 'canwe'

urlpatterns = [
    path('', index, name="index"),
]