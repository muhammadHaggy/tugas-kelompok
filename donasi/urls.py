from django.urls import path
from donasi.views import *

app_name = 'donasi'

urlpatterns = [
    path('', show_donasi, name='show_donasi'),
    path('get-data-donasi', get_data_donasi, name='get_data_donasi')
]