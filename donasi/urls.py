from django.urls import path
from donasi.views import *

app_name = 'donasi'

urlpatterns = [
    path('', show_donasi, name='show_donasi'),
    path('bayar/<int:id>', bayar_donasi, name='bayar_donasi'),
    path('bayar/proses/<int:id>', bayar_proses, name='bayar_proses'),
    path('get-data-donasi/', get_data_donasi, name='get_data_donasi'),
]