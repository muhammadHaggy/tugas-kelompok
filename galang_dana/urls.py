from unicodedata import name
from django.urls import path
from galang_dana.views import *

app_name = 'galang_dana'

urlpatterns = [
    path('', show_galang_dana, name='show_galang_dana'),
    path('create/', show_buat_galang_dana, name='show_buat_galang_dana'),
    path('get-user-count/', get_user_count_json, name='get_user_count'),
]