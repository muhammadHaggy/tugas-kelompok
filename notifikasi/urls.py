from django.urls import path
from notifikasi.views import show_notifikasi

app_name = 'notifikasi'

urlpatterns = [
    path('', show_notifikasi, name='show_notifikasi'),
]